PGDMP     $                    x            test_bookstore     12.3 (Ubuntu 12.3-1.pgdg20.04+1)     12.3 (Ubuntu 12.3-1.pgdg20.04+1) !    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16534    test_bookstore    DATABASE     �   CREATE DATABASE test_bookstore WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE test_bookstore;
                postgres    false            �            1259    16535    authors    TABLE     l   CREATE TABLE public.authors (
    id integer NOT NULL,
    name text NOT NULL,
    books text[] NOT NULL
);
    DROP TABLE public.authors;
       public         heap    postgres    false            �            1255    16541    fn_get_author(text)    FUNCTION     	  CREATE FUNCTION public.fn_get_author(p_author text) RETURNS SETOF public.authors
    LANGUAGE plpgsql
    AS $$BEGIN
RETURN QUERY
   SELECT authors."id",
   		  authors.name,
		  authors.books
   FROM public.authors
   WHERE public.authors.name = p_author;
END;$$;
 3   DROP FUNCTION public.fn_get_author(p_author text);
       public          postgres    false    202            �            1255    16542    fn_get_author_from_id(integer)    FUNCTION       CREATE FUNCTION public.fn_get_author_from_id(p_author_id integer) RETURNS SETOF public.authors
    LANGUAGE plpgsql
    AS $$BEGIN
RETURN QUERY
   SELECT authors."id",
   		  authors.name,
		  authors.books
   FROM public.authors
   WHERE public.authors."id" = p_author_id;
END;$$;
 A   DROP FUNCTION public.fn_get_author_from_id(p_author_id integer);
       public          postgres    false    202            �            1259    16543    books    TABLE     z   CREATE TABLE public.books (
    isbn text NOT NULL,
    name text NOT NULL,
    author text NOT NULL,
    year integer
);
    DROP TABLE public.books;
       public         heap    postgres    false            �            1255    16549    fn_get_book(text)    FUNCTION       CREATE FUNCTION public.fn_get_book(p_isbn text) RETURNS SETOF public.books
    LANGUAGE plpgsql
    AS $$BEGIN
RETURN QUERY
   SELECT books.isbn,
   		  books.name,
		  books.author,
		  books.year
   FROM public.books
   WHERE public.books.isbn = p_isbn;
END;$$;
 /   DROP FUNCTION public.fn_get_book(p_isbn text);
       public          postgres    false    203            �            1259    16550    users    TABLE     �   CREATE TABLE public.users (
    "Id" integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    mail text,
    role text
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1255    16556    fn_get_personnel(text, text)    FUNCTION     �  CREATE FUNCTION public.fn_get_personnel(name text, password text) RETURNS SETOF public.users
    LANGUAGE plpgsql
    AS $$BEGIN
RETURN QUERY
   SELECT personnel."Id",
   		  personnel.name,
		  personnel.password,
		  personnel.mail,
		  personnel.role
   FROM public.personnel
   WHERE public.personnel.name = fn_get_personnel.name
   AND public.personnel.password = fn_get_personnel.password;
END;$$;
 A   DROP FUNCTION public.fn_get_personnel(name text, password text);
       public          postgres    false    204            �            1255    16557    fn_get_user(text)    FUNCTION     2  CREATE FUNCTION public.fn_get_user(username text) RETURNS SETOF public.users
    LANGUAGE plpgsql
    AS $$BEGIN
RETURN QUERY
   SELECT users."Id",
   		  users.username,
		  users.password,
		  users.mail,
		  users.role
   FROM public.users
   WHERE public.users.username = fn_get_user.username;
END;$$;
 1   DROP FUNCTION public.fn_get_user(username text);
       public          postgres    false    204            �            1255    16558 +   fn_insert_personnel(text, text, text, text)    FUNCTION     r  CREATE FUNCTION public.fn_insert_personnel(name text, password text, mail text, role text) RETURNS void
    LANGUAGE plpgsql
    AS $$
    
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
$$;
 Z   DROP FUNCTION public.fn_insert_personnel(name text, password text, mail text, role text);
       public          postgres    false            �            1255    16559 $   fn_update_author_name(integer, text)    FUNCTION     �   CREATE FUNCTION public.fn_update_author_name(p_id integer, p_name text) RETURNS void
    LANGUAGE plpgsql
    AS $$
    
BEGIN
   UPDATE public.authors
	SET name = p_name
	WHERE authors."id" = p_id;
END
$$;
 G   DROP FUNCTION public.fn_update_author_name(p_id integer, p_name text);
       public          postgres    false            �            1259    16560    authors_id_seq    SEQUENCE     �   CREATE SEQUENCE public.authors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.authors_id_seq;
       public          postgres    false    202            �           0    0    authors_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.authors_id_seq OWNED BY public.authors.id;
          public          postgres    false    205            �            1259    16562    users_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."users_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public."users_Id_seq";
       public          postgres    false    204            �           0    0    users_Id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public."users_Id_seq" OWNED BY public.users."Id";
          public          postgres    false    206            �            1259    16564 	   personnel    TABLE     �   CREATE TABLE public.personnel (
    "Id" integer DEFAULT nextval('public."users_Id_seq"'::regclass) NOT NULL,
    name text NOT NULL,
    password text NOT NULL,
    mail text,
    role text
);
    DROP TABLE public.personnel;
       public         heap    postgres    false    206            )           2604    16571 
   authors id    DEFAULT     h   ALTER TABLE ONLY public.authors ALTER COLUMN id SET DEFAULT nextval('public.authors_id_seq'::regclass);
 9   ALTER TABLE public.authors ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    202            *           2604    16572    users Id    DEFAULT     h   ALTER TABLE ONLY public.users ALTER COLUMN "Id" SET DEFAULT nextval('public."users_Id_seq"'::regclass);
 9   ALTER TABLE public.users ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    206    204            �          0    16535    authors 
   TABLE DATA           2   COPY public.authors (id, name, books) FROM stdin;
    public          postgres    false    202   �(       �          0    16543    books 
   TABLE DATA           9   COPY public.books (isbn, name, author, year) FROM stdin;
    public          postgres    false    203   )       �          0    16564 	   personnel 
   TABLE DATA           E   COPY public.personnel ("Id", name, password, mail, role) FROM stdin;
    public          postgres    false    207   ))       �          0    16550    users 
   TABLE DATA           E   COPY public.users ("Id", username, password, mail, role) FROM stdin;
    public          postgres    false    204   F)       �           0    0    authors_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.authors_id_seq', 1, false);
          public          postgres    false    205            �           0    0    users_Id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public."users_Id_seq"', 32, true);
          public          postgres    false    206            5           2606    16574    personnel AK_personel_username 
   CONSTRAINT     [   ALTER TABLE ONLY public.personnel
    ADD CONSTRAINT "AK_personel_username" UNIQUE (name);
 J   ALTER TABLE ONLY public.personnel DROP CONSTRAINT "AK_personel_username";
       public            postgres    false    207            1           2606    16576    users AK_users_username 
   CONSTRAINT     X   ALTER TABLE ONLY public.users
    ADD CONSTRAINT "AK_users_username" UNIQUE (username);
 C   ALTER TABLE ONLY public.users DROP CONSTRAINT "AK_users_username";
       public            postgres    false    204            -           2606    16578    authors authors_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.authors DROP CONSTRAINT authors_pkey;
       public            postgres    false    202            /           2606    16580    books books_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (isbn);
 :   ALTER TABLE ONLY public.books DROP CONSTRAINT books_pkey;
       public            postgres    false    203            7           2606    16582    personnel personel_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.personnel
    ADD CONSTRAINT personel_pkey PRIMARY KEY ("Id");
 A   ALTER TABLE ONLY public.personnel DROP CONSTRAINT personel_pkey;
       public            postgres    false    207            3           2606    16584    users users_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY ("Id");
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    204            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     