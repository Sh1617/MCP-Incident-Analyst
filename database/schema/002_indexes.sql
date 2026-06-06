CREATE INDEX idx_incidents_incident_id
ON incidents(incident_id);

CREATE INDEX idx_incidents_status
ON incidents(status);

CREATE INDEX idx_investigations_incident_id
ON investigations(incident_id);

CREATE INDEX idx_reports_investigation_id
ON reports(investigation_id);

CREATE INDEX idx_feedback_report_id
ON feedback(report_id);

CREATE INDEX idx_conversation_session
ON conversation_history(session_id);

CREATE INDEX idx_findings_investigation
ON investigation_findings(investigation_id);

CREATE INDEX idx_tool_execution_investigation
ON tool_executions(investigation_id);

CREATE INDEX idx_agent_execution_investigation
ON agent_executions(investigation_id);