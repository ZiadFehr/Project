import cv2
import torch
import boto3
import time
import csv
import uuid
from datetime import datetime

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', source='local')
model.conf = 0.5

sns = boto3.client('sns', region_name='us-east-1')
s3 = boto3.client('s3')
TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:mask-alerts'
S3_BUCKET = 'your-s3-bucket-name'

cap = cv2.VideoCapture(0)

def send_alert():
    timestamp = datetime.utcnow().isoformat()
    message = f"🚨 ALERT: Person without mask detected at {timestamp}"
    sns.publish(TopicArn=TOPIC_ARN, Message=message, Subject="Mask Alert")

def log_detection(label, confidence):
    with open('detection_log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.utcnow().isoformat(), label, f"{confidence:.2f}"])

def upload_to_s3(frame):
    filename = f"{uuid.uuid4()}.jpg"
    cv2.imwrite(filename, frame)
    s3.upload_file(filename, S3_BUCKET, f'violations/{filename}')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = results.pandas().xyxy[0]

    for _, row in detections.iterrows():
        label = row['name']
        confidence = float(row['confidence'])
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])

        color = (0, 255, 0) if label == 'mask' else (0, 0, 255)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        log_detection(label, confidence)

        if label == 'no_mask' and confidence > 0.6:
            send_alert()
            upload_to_s3(frame)
            print("🚨 ALERT SENT")
            time.sleep(5)
            break

    cv2.imshow("Mask Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()