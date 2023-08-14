# Pool facts

This AWS Lambda function fetches a random line from a publicly available text file on the web and sends it to a configured webhook. This can be useful for notifications, reminders, or any other application where you want to send random text data to a webhook at scheduled intervals.

## Setup Instructions

### 1. **Set Up AWS Lambda**:
   - Navigate to the AWS Management Console.
   - Go to **Services** > **Lambda**.
   - Click on **Create function**.
   - Choose **Author from scratch**, give your function a name, and set the runtime to **Python 3.x**.
   - For the execution role, choose **Create a new role from AWS policy templates** and give your role a name.
   - Click on **Create function**.

### 2. **Add the Python Code**:
   - Copy the provided Python script.
   - In the AWS Lambda dashboard, paste the script into the inline code editor for your function.

### 3. **Set Environment Variables**:
   - In the **Configuration** tab of your Lambda function, find the **Environment variables** section.
   - Click on **Edit**.
   - Add two new environment variables:
     - `WEBHOOK_URL`: Set its value to your webhook URL.
     - `TEXT_FILE_URL`: Set its value to your text file's URL.
   - Click on **Save**.

### 4. **Set up a CloudWatch Events Trigger**:
   - Navigate to the **Designer** section of your Lambda function.
   - Click on **Add trigger**.
   - Choose **CloudWatch Events**.
   - Create a new rule.
   - For the cron expression, use `0 */12 * * ? *` to make the function execute once every 12 hours.
   - Enable the trigger.
   - Click on **Add**.

### 5. **Test & Deploy**:
   - Save your Lambda function.
   - Click on **Test** to see if a message is sent to your webhook.

## Conclusion
Once set up, this function will automatically fetch a random line from your specified text file and send it to your webhook every 12 hours. Adjust the CloudWatch Events cron expression if you desire a different frequency.

