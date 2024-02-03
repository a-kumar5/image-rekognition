import boto3


def moderate_image(photo, bucket):
    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')

    response = client.detect_moderation_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})

    print('Detected labels for ' + photo)
    print('response:', response)
    for label in response['ModerationLabels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))
        print(label['ParentName'])
    return len(response['ModerationLabels'])


def main():

    photo = 'smoke.jpeg'
    bucket = 'food-image-upload'
    label_count = moderate_image(photo, bucket)
    print("Labels detected: " + str(label_count))

if __name__ == "__main__":
    main()