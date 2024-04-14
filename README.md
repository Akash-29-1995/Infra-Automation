Objective:

● Write a script (bash, Python, or your preferred language) to automate the backup of an AWS S3
bucket.
●Implement a process to scale EC2 instances based on CPU utilization automatically.

Task 1: For automation of back of s3 I have used the boto3 script in Python and used it in lambda, since I assumed that this would be a repetitive task so need an event bridge also to schedule the job. I have provided the code in the s3-backup.py file which is pushed to this repository. Apart from this, I have mentioned the steps below to achieve this:


A. Create a lambda function with the name s3-bucket-backup.
![Screenshot from 2024-04-12 21-12-39](https://github.com/Akash-29-1995/Infra-Automation/assets/45091399/d293512d-df2d-4ded-a3c9-2282d1177286)

B. Set the runtime to Python 3.12 ( or your preferred language and its version ) and architecture Make the changes in timeout time to at least 5 minutes so that you will not get a timeout error.
![Screenshot from 2024-04-12 21-14-07](https://github.com/Akash-29-1995/Infra-Automation/assets/45091399/4a630def-8b02-46e0-9c56-3fc78da94809)

C. In the Python script where you need to define the source bucket and target bucket.



Task 2: please find below the steps to achieve CPU utilization-based autoscaling.

A. Create launch temp as per below screenshot:
 
![Screenshot from 2024-04-12 21-24-02](https://github.com/Akash-29-1995/Infra-Automation/assets/45091399/64c43e91-b2ec-4e11-baa1-1c931dfacfc3)

B. create autoscaling group and choose the launch template
![Screenshot from 2024-04-12 21-24-02](https://github.com/Akash-29-1995/Infra-Automation/assets/45091399/7f637d67-d577-4b1c-9f37-9e844e1dbf04)

![Screenshot from 2024-04-12 21-25-10](https://github.com/Akash-29-1995/Infra-Automation/assets/45091399/ab1a94df-75ac-45b5-82f6-829540264e65)

![Screenshot from 2024-04-12 21-25-45](https://github.com/Akash-29-1995/Infra-Automation/assets/45091399/f45cc919-4d9c-446d-b2fc-4937fbab1d40)

C. Use the target tracking policy to implement condition-based autoscaling. Like in this case CPU utilisation and choose the utilisation limit so that based on that autoscale triggered and launch new instances.

![Screenshot from 2024-04-12 21-26-15](https://github.com/Akash-29-1995/Infra-Automation/assets/45091399/19bb2418-bee4-4ee9-ae88-ccf4d905e3b7)

