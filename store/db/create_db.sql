CREATE TABLE public.authors
(
    id integer NOT NULL DEFAULT nextval('authors_id_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    books text[] COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT authors_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.authors
    OWNER to postgres;


CREATE TABLE public.books
(
    isbn text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    author text COLLATE pg_catalog."default" NOT NULL,
    year integer,
    CONSTRAINT books_pkey PRIMARY KEY (isbn)
)

TABLESPACE pg_default;

ALTER TABLE public.books
    OWNER to postgres;

CREATE TABLE public.personnel
(
    "Id" integer NOT NULL DEFAULT nextval('"users_Id_seq"'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    mail text COLLATE pg_catalog."default",
    role text COLLATE pg_catalog."default",
    CONSTRAINT personel_pkey PRIMARY KEY ("Id"),
    CONSTRAINT "AK_personel_username" UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE public.personnel
    OWNER to postgres;

CREATE TABLE public.users
(
    "Id" integer NOT NULL DEFAULT nextval('"users_Id_seq"'::regclass),
    username text COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    mail text COLLATE pg_catalog."default",
    role text COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY ("Id"),
    CONSTRAINT "AK_users_username" UNIQUE (username)
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;

CREATE OR REPLACE FUNCTION public.fn_get_author(
	p_author text)
    RETURNS SETOF authors
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
    ROWS 1000

AS $BODY$BEGIN
RETURN QUERY
   SELECT authors."id",
   		  authors.name,
		  authors.books
   FROM public.authors
   WHERE public.authors.name = p_author;
END;$BODY$;

ALTER FUNCTION public.fn_get_author(text)
    OWNER TO postgres;


CREATE OR REPLACE FUNCTION public.fn_get_author_from_id(
	p_author_id integer)
    RETURNS SETOF authors
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
    ROWS 1000

AS $BODY$BEGIN
RETURN QUERY
   SELECT authors."id",
   		  authors.name,
		  authors.books
   FROM public.authors
   WHERE public.authors."id" = p_author_id;
END;$BODY$;

ALTER FUNCTION public.fn_get_author_from_id(integer)
    OWNER TO postgres;

CREATE OR REPLACE FUNCTION public.fn_get_book(
	p_isbn text)
    RETURNS SETOF books
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
    ROWS 1000

AS $BODY$BEGIN
RETURN QUERY
   SELECT books.isbn,
   		  books.name,
		  books.author,
		  books.year
   FROM public.books
   WHERE public.books.isbn = p_isbn;
END;$BODY$;

ALTER FUNCTION public.fn_get_book(text)
    OWNER TO postgres;

CREATE OR REPLACE FUNCTION public.fn_get_personnel(
	name text,
	password text)
    RETURNS SETOF users
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
    ROWS 1000

AS $BODY$BEGIN
RETURN QUERY
   SELECT personnel."Id",
   		  personnel.name,
		  personnel.password,
		  personnel.mail,
		  personnel.role
   FROM public.personnel
   WHERE public.personnel.name = fn_get_personnel.name
   AND public.personnel.password = fn_get_personnel.password;
END;$BODY$;

ALTER FUNCTION public.fn_get_personnel(text, text)
    OWNER TO postgres;

CREATE OR REPLACE FUNCTION public.fn_get_user(
	username text)
    RETURNS SETOF users
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
    ROWS 1000

AS $BODY$BEGIN
RETURN QUERY
   SELECT users."Id",
   		  users.username,
		  users.password,
		  users.mail,
		  users.role
   FROM public.users
   WHERE public.users.username = fn_get_user.username;
END;$BODY$;

ALTER FUNCTION public.fn_get_user(text)
    OWNER TO postgres;

CREATE OR REPLACE FUNCTION public.fn_insert_personnel(
	name text,
	password text,
	mail text,
	role text)
    RETURNS void
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE

AS $BODY$

BEGIN
   INSERT INTO public.personnel(
	   name,
	   password,
	   mail,
	   role)
	VALUES (fn_insert_personnel.name,
		    fn_insert_personnel.password,
		    fn_insert_personnel.mail,
		   	fn_insert_personnel.role);
END
$BODY$;

ALTER FUNCTION public.fn_insert_personnel(text, text, text, text)
    OWNER TO postgres;

CREATE OR REPLACE FUNCTION public.fn_update_author_name(
	p_id integer,
	p_name text)
    RETURNS void
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE

AS $BODY$

BEGIN
   UPDATE public.authors
	SET name = p_name
	WHERE authors."id" = p_id;
END
$BODY$;

ALTER FUNCTION public.fn_update_author_name(integer, text)
    OWNER TO postgres;
