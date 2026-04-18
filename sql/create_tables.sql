-- ============================================
-- create_tables.sql
-- Schéma pour charger le dataset dans BigQuery
-- (si tu veux brancher Looker Studio via BigQuery
-- au lieu de l'upload CSV direct).
-- ============================================

CREATE SCHEMA IF NOT EXISTS `teen_mental_health`;

CREATE OR REPLACE TABLE `teen_mental_health.survey_responses` (
    respondent_id          INT64      NOT NULL,
    age                    INT64      NOT NULL,
    gender                 STRING     NOT NULL,
    daily_social_media_hours FLOAT64  NOT NULL,
    platform_usage         STRING     NOT NULL,
    sleep_hours            FLOAT64    NOT NULL,
    screen_time_before_sleep FLOAT64  NOT NULL,
    academic_performance   FLOAT64    NOT NULL,
    physical_activity      FLOAT64    NOT NULL,
    social_interaction_level STRING   NOT NULL,
    stress_level           INT64      NOT NULL,
    anxiety_level          INT64      NOT NULL,
    addiction_level        INT64      NOT NULL,
    depression_label       INT64      NOT NULL,

    -- Variables dérivées
    age_group              STRING,
    screen_time_category   STRING,
    sleep_quality          STRING,
    mental_health_score    FLOAT64
);

-- Commentaires descriptifs
ALTER TABLE `teen_mental_health.survey_responses`
    SET OPTIONS (
        description = "Dataset sur la santé mentale des adolescents — 1 200 observations"
    );