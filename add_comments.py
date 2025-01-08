from jira import JIRA
import os

# JIRA server details
jira_server = 'https://youremail.atlassian.net/'  # Replace with your JIRA URL
jira_user = 'youremail@gmail.com'  # Replace with your JIRA username/email
jira_api_token = 'yourapitoken'  # Replace with your JIRA API token

# Initialize JIRA client
try:
    jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_api_token))
    print("Successfully connected to JIRA!")
except Exception as e:
    print(f"Failed to connect to JIRA: {e}")
    exit(1)  # Exit the script if connection fails

# List of issues
issue_keys = ['SCRUM-1', 'SCRUM-2', 'SCRUM-3', 'SCRUM-4', 'SCRUM-5', 'SCRUM-6']

# Comment to be added
comment_text = "Blocked for now. Waiting for approval."

# Add comment to each issue
for issue_key in issue_keys:
    print(f"Processing issue: {issue_key}")
    try:
        jira.add_comment(issue_key, comment_text)
        print(f"Comment added to {issue_key}")
    except Exception as e:
        print(f"Failed to add comment to {issue_key}. Error: {e}")

print("Script finished successfully!")
