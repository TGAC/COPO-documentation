.. _tol-profile-walkthrough:

=======================
Tree of Life Profile
=======================

In COPO, a :abbr:`ToL (Tree of Life)` [#f1]_ work profile [#f2]_ is required to submit research objects [#f3]_ such as
samples.

---------------------------------------------
Steps to Create a Tree of Life Profile
---------------------------------------------

#. Click the |add-profile-button| **Add new record** icon to view the **Add Profile** form

    .. figure:: /assets/images/profile/profile_add_record_button_web_page.png
      :alt: Add new profile record button
      :align: center
      :target: /assets/images/profile/profile_add_record_button_web_page.png
      :class: with-shadow with-border

      **ToL Profile: Add new profile record icon**

#. **Contact COPO via email** dialogue is displayed indictating that the user is not a member of any manifest group
   and that the user must make a request to be added to a manifest group to make ToL manifest submissions
   if the user would like to do so.

   Click **Okay** to close the dialogue.

    .. figure:: /assets/images/profile/profile_contact_copo_prompt_for_group_access.png
      :alt: Contact COPO dialogue
      :align: center
      :target: /assets/images/profile/profile_contact_copo_prompt_for_group_access.png
      :class: with-shadow with-border

      **ToL Profile: Contact COPO dialogue is displayed regarding getting access to make ToL manifest
      submissions**

#. Provide details for the new profile then, click **Save**

    .. note::
       The **Profile type** dropdown menu will only display the **Stand-alone** option.
       :email:`Contact the COPO team <ei.copo@earlham.ac.uk>` inorder to be added to a desired profile group and be
       granted access to choose your desired profile type.

    .. figure:: /assets/images/profile/profile_add_profile_form_web_page_tol.png
      :alt: Add profile form
      :align: center
      :target: /assets/images/profile/profile_add_profile_form_web_page_tol.png
      :class: with-shadow with-border

      **ToL Profile: Add profile form dialogue**

    .. raw:: html

       <br>

    .. hint::

      Both profile **Title** and profile **Description** are mandatory form fields.

      Meaningful field values are recommended in the form boxes because the information will appear
      in submissions of the research objects [#f2]_ associated with the profile, in public remote repositories.

    .. raw:: html

       <br>

    .. figure:: /assets/images/profile/profile_add_profile_form_web_page_tol.png
      :alt: Choose profile type on add profile form
      :align: center
      :target: /assets/images/profile/profile_add_profile_form_web_page_tol.png
      :class: with-shadow with-border

      **ToL Profile form: Choose profile type**

    .. raw:: html

       <br>

    .. figure:: /assets/images/profile/profile_add_profile_form_web_page_tol.png
      :alt: Choose associated profile type or subproject on add profile form
      :align: center
      :target: /assets/images/profile/profile_add_profile_form_web_page_tol.png
      :class: with-shadow with-border

      **ToL Profile form: Choose associated profile type or a subproject**

   More than one associated type or subproject can be chosen.

    .. raw:: html

       <br>

#. The new profile will be displayed in the **Profile** list

    .. figure:: /assets/images/profile/profile_tol_profile_created.png
      :alt: Stand-alone profile created
      :align: center
      :target: /assets/images/profile/profile_tol_profile_created.png
      :class: with-shadow with-border

      **Stand-alone Profile: Work profiles' web page displaying the created profile**

    .. raw:: html

       <br>

    .. hint::

      The **Work Profiles**' list can be sorted by date created, profile title or profile type.

      Choose the desired sort type from the **Sort by** dropdown menu (at the top-right of the profile record).

.. seealso::

   * See :ref:`Steps to create Stand-alone profile <standalone-profile-walkthrough>` if you would like to make other
     submissions

.. raw:: html

   <hr>

.. _tol-profile-components:

-------------------
Profile Components
-------------------

A COPO profile defines a set of component types from which instances of research objects can be created.

The following component types are currently defined:

#. :doc:`Samples <samples>`
#. :doc:`Accessions <accessions-component-tol>`

.. figure:: /assets/images/profile/profile_tol_profile_components.png
   :alt: Tree of Life profile components
   :align: center
   :target: /assets/images/profile/profile_tol_profile_components.png
   :class: with-shadow with-border

   **Tree of Life Profile Components**

* Component instances defined within a profile will only be visible within that profile [#f2]_.

* To access a component within a profile, click the component button displayed within the profile box after the
  |profile-components-button| profile **Components** button was clicked (see the screenshot above).

* The number beside each component button represents the number of items or instances of the component added or created.


.. rubric:: Footnotes
.. [#f1] See: :term:`Tree of Life (ToL) <T>`.
.. [#f2] Also known as COPO profile. See: :term:`COPO profile/work profile<C>`.
.. [#f3] Research objects refer to files, reads, assemblies, files and sequence annotations.
         A Stand-alone profile is considered as a *project* research object.
         See: :term:`Profile component<P>`.
   

..
    Images declaration
..
.. |add-profile-button| image:: /assets/images/profile/profile_add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/profile/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link
   



