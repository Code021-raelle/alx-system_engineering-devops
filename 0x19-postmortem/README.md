## Outage Postmortem: The Great Emoji Outbreak

# Issue Summary:
Duration: May 10, 2024, 12:00 PM UTC to May 11, 2024, 3:00 AM UTC
Impact: Slack service degraded, users experienced delays and missing emojis. 60% of users were affected.
Root Cause: Overload of emoji reactions triggering a cascading failure in message rendering.

# Timeline:
* May 10, 2024, 12:00 PM UTC: Issue detected by monitoring alert indicating elevated server CPU usage.
* 12:15 PM UTC: Investigation began, suspecting a possible DDoS attack due to high incoming requests.
* 2:00 PM UTC: Engineers found no evidence of a DDoS attack but noticed unusual patterns in emoji usage.
* 4:30 PM UTC: Incident escalated to the backend services team as the issue seemed related to message rendering.
* 6:00 PM UTC: Debugging continued, focusing on message rendering components.
* May 11, 2024, 1:00 AM UTC: Root cause identified - excessive emoji reactions causing rendering delays.
* 2:30 AM UTC: Temporary fix implemented to limit the number of emoji reactions per message.

# Root Cause and Resolution:
The root cause of the outage was the overwhelming number of emoji reactions to messages, causing a bottlenect in the message rendering process. The system was not equipped to handle such a high volume of emoji reactions efficiently. To resolve the issue, we implemented a temporary fix to limit the number of emoji reactions allowed per message. This alleviated the rendering bottleneck and restored normal service functionality.

# Corrective and Preventive Measures:
To prevent similar outages in the future, we will inmplement the following measures:
* Optimize Message Rendering: Improve the efficiency of the message rendering process to handle high loads more gracefully.
* Enhance Monitoring: Enhance monitoring tools to better detect unusual patterns in system usage, such as sudden spikes in emoji reactions.
* Automated Scaling: Implement automated scaling mechanisms to dynamically allocate resources based on system load, ensuring smooth operation during peak usage periods.

# Conclusion:
The Great Emoji Outbreak of 2024 taught us valuable lessons about the importance of monitoring system usage patterns and optimizing critical components for scalability. By implementing proactive measures and continously improving our infrastructure, we aim to provide a more resilent and reliable service to our users.

### For more details and updates, check out our [GitHub repository](https://github.com/Code021-raelle).