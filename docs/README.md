# Milestone 1

## User Stories

The **User Stories** for site visitors, members, and site administrator are listed below.  The **Acceptance Criteria** are listed in-line with each story.


### Unauthenticated User

1. As a _visitor_ to the Dead List I want to _browse_ recent celebrity deaths in order to _learn about them_ and read the puns that members of the site made about them.
 * **Acceptance Criteria:**
   * The site has proper views that display each call that was made.
   * The views contain images and biographical information about the deceased.

### Authenticated User

2. As a _member_ of the Dead List, I want to be able to _post_ (`call`) a new death _in order to be the first person to do so_.
 * **Acceptance Criteria:**
   * Members can click on the `Make Call` button and enter the necessary information to add a new post.

3. As a _member_ of the Dead List, I want to be able to _edit_ any posts (`puns`) I make _in order to clarify intent or correct mistakes_.
 * **Acceptance Criteria:**
   * Members can select and edit their own calls or puns for clarity or to add more information.

4. As a _member_ of the Dead List, I want to be able to _respond_ to other users posts (`calls`), _in order to share puns_.
 * **Acceptance Criteria:**
   * Members are able to add or make puns related to a given call.

5. As a _member_ of the Dead List, I want to be able to _rate_ other users comments (`puns`) _in order to show my appreciation or aversion_ for their humor.
 * **Acceptance Criteria:**
   * Members are able to up or down vote puns other users make on a given call.
   * Ratings are displayed next to each pun

### Administrator User

6. As the _administrator_ of the Dead List, I want to be able to _manage_ users of the site (remove) _in order to maintain a positive environment_.
 * **Acceptance Criteria:**
   * The administrator is able to remove / delete a user from the site.

7. As the _administrator_ of the Dead List, I want to be able to _manage_ (edit) posts (calls / puns) made to the site _in order to ensure negative or offensive content isn't shared_.
 * **Acceptance Criteria:**
   * The administrator is able to remove any call or pun made.
   * The administrator is able to update the content of any call or pun made.

----

### Mis-user Stories

The **Mis-user Stories** for a mischievous member, disgruntled member, cheating member are listed below.  The **Mitigation Criteria** are listed in-line with each story.

1. As a _mischievous member_ I want to _deface the site_ by _inserting malicious code_ when posting.
 * Mitigation Criteria:
   * Validate input from all fields.
   * Use Object-Relational Mapping instead of raw SQL when communicating with the DB.

2. As a _disgruntled member_ I want to _redirect visitors_ to a malicious site by _adding new HTML/JS_ via text fields.
 * Mitigation Criteria:
   * Ensure input is properly escaped.

3. As a _cheating member_ I want to _add upvotes_ of my posts by _editing my rating count_.
 * Mitigation Criteria:
   * Ensure proper permissions exist so users can only modify specific fields of their own posts.

----

## Diagrams

### Interface Diagrams

The following images are the initial UI design mockups.  They are subject to change based on the technical implementation.

#### Main View

![Main View](https://github.com/TravisIngram/Dead-List/blob/main/docs/imgs/DL_01_Main.png)

#### Call Detail View

![Call Detail View](https://github.com/TravisIngram/Dead-List/blob/main/docs/imgs/DL_02_call_detail.png)

#### All Calls View

![All Calls View](https://github.com/TravisIngram/Dead-List/blob/main/docs/imgs/DL_03_all_calls.png)

#### Make Call View

![Make Call View](https://github.com/TravisIngram/Dead-List/blob/main/docs/imgs/DL_04_make_call.png)

### Architectural Diagrams (C4)

#### Level 1: System Context Diagram

![System Context Diagram](https://github.com/TravisIngram/Dead-List/blob/main/docs/imgs/DL_C4_Context.png)

#### Level 2: Container Diagram

![Container Diagram](https://github.com/TravisIngram/Dead-List/blob/main/docs/imgs/DL_C4_Container.png)

#### Level 3: Component Diagram

![Component Diagram](https://github.com/TravisIngram/Dead-List/blob/main/docs/imgs/DL_C4_Component.png)