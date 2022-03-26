create schema if not exists park_tickets;

create extension if not exists "uuid-ossp";

create table if not exists park_tickets.person (
    id uuid default uuid_generate_v4() primary key,
    name text not null,
    created_at timestamp not null default now(),
    updated_at timestamp not null default now()
);

create table if not exists park_tickets.plate (
    id uuid default uuid_generate_v4() primary key,
    plate_number text not null,
    start_date timestamp not null,
    end_date timestamp not null,
    created_at timestamp not null default now(),
    updated_at timestamp not null default now()
);

create table if not exists park_tickets.person_plate (
    person_id uuid references park_tickets.person(id) on delete cascade,
    plate_id uuid references park_tickets.plate(id) on delete cascade
);
