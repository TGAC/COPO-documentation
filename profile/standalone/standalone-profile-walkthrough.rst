.. _standalone-profile-walkthrough:

====================
Stand-alone Profile
====================
In COPO, a Stand-alone work profile [#f1]_ is required to submit files, reads, assemblies and sequence annotations.

---------------------------------------------
Steps to Create a Stand-alone Profile
---------------------------------------------

#. Click the |add-profile-button| **Add new record** icon to view the **Add Profile** form

    .. figure:: /_static/images/profile/profile_add_record_button_web_page.png
      :alt: Add new profile record button
      :align: center
      :target: /_static/images/profile/profile_add_record_button_web_page.png
      :class: with-shadow with-border

      **Stand-alone Profile: Add new profile record icon**

#. **Contact COPO via email** dialogue is displayed indictating that the user is not a member of any manifest group
   and that the user must make a request to be added to a manifest group to make ToL manifest submissions
   if the user would like to do so.

   Click **Okay** to close the dialogue.

    .. note::

       Submissions such as files, reads, assemblies, files and sequence annotations can only be made using a
       Stand-alone profile type.

    .. figure:: /_static/images/profile/profile_contact_copo_prompt_for_group_access.png
      :alt: Contact COPO dialogue
      :align: center
      :target: /_static/images/profile/profile_contact_copo_prompt_for_group_access.png
      :class: with-shadow with-border

      **Stand-alone Profile: Contact COPO dialogue is displayed regarding getting access to make ToL manifest
      submissions**

#. Provide details for the new profile then, click **Save**

    .. figure:: /_static/images/profile/profile_add_profile_form_web_page_standalone.png
      :alt: Add profile form
      :align: center
      :target: /_static/images/profile/profile_add_profile_form_web_page_standalone.png
      :class: with-shadow with-border

      **Stand-alone Profile: Add profile form dialogue**

    .. raw:: html

       <br>

    .. hint::

      Both profile **Title** and profile **Description** are mandatory form fields.

      Meaningful field values are recommended in the form boxes because the information will appear
      in submissions of the research objects [#f2]_ associated with the profile, in public remote repositories.

#. The new profile will be displayed in the **Profile** list

    .. figure:: /_static/images/profile/profile_standalone_profile_created.png
      :alt: Stand-alone profile created
      :align: center
      :target: /_static/images/profile/profile_standalone_profile_created.png
      :class: with-shadow with-border

      **Stand-alone Profile: Work profiles' web page displaying the created profile**

    .. raw:: html

       <br>

    .. hint::

      The **Work Profiles**' list can be sorted by date created, profile title or profile type.

      Choose the desired sort type from the **Sort by** dropdown menu (at the top-right of the profile record).

.. seealso::

   * See :ref:`Steps to create Tree of Life (ToL) profile <tol-profile-walkthrough>` if you would like to make ToL
     manifest submissions

.. raw:: html

   <hr>

.. _standalone-profile-components:

-----------------------------------
Stand-alone Profile Components
-----------------------------------

A COPO profile defines a set of component types from which instances of research objects can be created.

The following component types are currently defined:

   #. :ref:`Files <files>`
   #. :ref:`Reads <reads>`
   #. :ref:`Assembly <assemblies>`
   #. :ref:`Sequence Annotations <sequence-annotations>`
   #. :doc:`Accessions <accessions-component-standalone>`

.. figure:: /_static/images/profile/profile_standalone_profile_components.png
   :alt: Stand-alone profile components
   :align: center
   :target: /_static/images/profile/profile_standalone_profile_components.png
   :class: with-shadow with-border

   **Stand-alone Profile Components**

* Component instances defined within a profile will only be visible within that profile [#f1]_. 

* To access a component within a profile, click the component button displayed within the profile box after the
  |profile-components-button| profile **Components** button was clicked (see the screenshot above).

* The number beside each component button represents the number of items or instances of the component added or created.


.. rubric:: Footnotes
.. [#f1] Also known as COPO profile. See: :term:`COPO profile/work profile<C>`.
.. [#f2] Research objects refer to files, reads, assemblies, files and sequence annotations. A Stand-alone profile is
   considered as a *project* research object. See: :term:`Profile component<P>`.

..
    Images declaration
..
.. |add-profile-button| image:: /_static/images/profile/profile_add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /_static/images/profile/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link




   



