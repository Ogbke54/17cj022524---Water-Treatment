-- Table: public.kexx

-- DROP TABLE IF EXISTS public.kexx;

CREATE TABLE IF NOT EXISTS public.kexx
(
    "Country" text COLLATE pg_catalog."default" NOT NULL,
    "Year" integer,
    "Value" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.kexx
    OWNER to postgres;