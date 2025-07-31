# Automation Process Overview

These instructions describe the automated workflow for managing client and patient records as requested by the state. The process ensures secure handling of data and centralized storage within a cloud drive.

## 1. Worker Checklist
1. Retrieve the list of clients from the state order.
2. For each client, locate the most recent document in the cloud drive.
3. Update any information requested by the state in the document.
4. Save the updated document as a new version, retaining the previous copy.

## 2. Secure Email Procedure
1. After updating, generate an encrypted email to the state with the updated files.
2. Use the approved secure email service to send the data.
3. Confirm delivery by monitoring the "sent" folder or automatic receipt notifications.

## 3. Cloud Drive Organization
1. Within the shared Google Drive, create folders for each client.
2. Store old documents in an `archive` subfolder.
3. Keep the updated version directly under the client folder.
4. Apply consistent naming, for example:
   - `client-name/YYYY-MM-DD_record_v1.docx` for the archived version.
   - `client-name/current_record.docx` for the active file.

## 4. Tagging System
1. Use Google Drive labels to tag documents with their status:
   - `Pending Update`
   - `Updated`
   - `Archived`
2. Tags help locate documents quickly and ensure compliance with the request from the state.

## 5. Web Application
1. Access the application from any browser using the provided URL.
2. The app displays orders from the state, client lists, and required documents.
3. Workers can update records directly in the app. The app automatically stores them in Google Drive and applies the correct tags.
4. Users with the appropriate role can see audit logs and verify what data was sent.

## 6. Getting Started
1. Log in to the shared Google Workspace using your company credentials.
2. Open the web app and navigate to the "Orders" page.
3. For each client record, click "Edit" to update the document as needed.
4. Save your changes and confirm that the record is tagged `Updated`.
5. Select "Send to State" to trigger the secure email process.
6. Review sent items to confirm successful delivery.

## 7. Additional Tips
- Make sure to review archived files periodically and remove old records if required by retention policies.
- If the web app becomes unavailable, manual updates can still be performed directly in Google Drive following the organization and tagging guidelines above.

