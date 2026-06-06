CREATE TABLE incidents (
    id SERIAL PRIMARY KEY,

    incident_id VARCHAR(100) UNIQUE NOT NULL,

    title VARCHAR(255) NOT NULL,

    description TEXT,

    status VARCHAR(50) NOT NULL DEFAULT 'OPEN',

    severity VARCHAR(20) NOT NULL DEFAULT 'MEDIUM',

    source VARCHAR(100),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE investigations (
    id SERIAL PRIMARY KEY,

    investigation_id VARCHAR(100) UNIQUE NOT NULL,

    incident_id INTEGER NOT NULL REFERENCES incidents(id),

    user_query TEXT NOT NULL,

    status VARCHAR(50) NOT NULL DEFAULT 'RUNNING',

    confidence_score FLOAT DEFAULT 0.0,

    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    completed_at TIMESTAMP
);


CREATE TABLE reports (
    id SERIAL PRIMARY KEY,

    report_id VARCHAR(100) UNIQUE NOT NULL,

    investigation_id INTEGER NOT NULL
        REFERENCES investigations(id),

    executive_summary TEXT,

    timeline JSONB,

    evidence_collected JSONB,

    root_cause TEXT,

    contributing_factors JSONB,

    impact_analysis TEXT,

    remediation_steps JSONB,

    prevention_recommendations JSONB,

    confidence_score FLOAT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,

    report_id INTEGER NOT NULL
        REFERENCES reports(id),

    rating INTEGER CHECK (
        rating >= 1 AND rating <= 5
    ),

    comments TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE conversation_history (
    id SERIAL PRIMARY KEY,

    session_id VARCHAR(255) NOT NULL,

    role VARCHAR(20) NOT NULL,

    message TEXT NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE investigation_findings (
    id SERIAL PRIMARY KEY,

    investigation_id INTEGER NOT NULL
        REFERENCES investigations(id),

    agent_name VARCHAR(100) NOT NULL,

    finding_type VARCHAR(100),

    finding_content JSONB,

    confidence_score FLOAT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE tool_executions (
    id SERIAL PRIMARY KEY,

    investigation_id INTEGER NOT NULL
        REFERENCES investigations(id),

    agent_name VARCHAR(100),

    tool_name VARCHAR(100),

    execution_status VARCHAR(50),

    latency_ms INTEGER,

    tool_input JSONB,

    tool_output JSONB,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE agent_executions (
    id SERIAL PRIMARY KEY,

    investigation_id INTEGER NOT NULL
        REFERENCES investigations(id),

    agent_name VARCHAR(100),

    execution_status VARCHAR(50),

    latency_ms INTEGER,

    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    completed_at TIMESTAMP
);