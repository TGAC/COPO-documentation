.. _sample-managers-guidelines:

====================
Sample Managers
====================

This section gives an overview of the COPO features that are delegated to sample managers [#f1]_ who are responsible
for accepting or rejecting samples produced by sample submitters [#f2]_.

.. note::

   * Make a request to the :email:`COPO team <ei.copo@earlham.ac.uk>` indicating the type of profile manifest group
     that you would like to be assigned to as a sample manager and the associated profile type.

     The permission will be granted after the request has been approved.

.. seealso::

   * :ref:`View images produced by sample submitters <image-submission-view-images-sample-managers>`
   * :ref:`Download permits produced by sample submitters <permits-submission-download-permits-sample-managers>`
   * :ref:`Sample managers' Frequently Asked Questions <faq-sample-managers>`
   * :ref:`Profile types and associated profile types brokered through COPO <copo-project-affiliations>`

.. raw:: html

  <br>

.. _accessing-accept-reject-samples-web-page:

Accessing the Accept or Reject Samples web page
-----------------------------------------------

.. note::

  The |accept-reject-samples-navigation-button| button will only appear on the web page if you
  are granted permission to be a sample manager.

  Once the button is clicked, the **accept/reject samples** web page will be displayed.

If you have been granted permission as a sample manager, you will receive an email
notifying you that sample(s) has been submitted after a user uploads a manifest.

Similarly, you will receive an email when samples have been rejected.

Click the |accept-reject-samples-navigation-button| button to navigate to the web page to accept or reject samples.

Alternatively, navigate to `Accept/Reject Samples web page <https://copo-project.org/copo/dtol_submission/accept_reject_sample>`__.

.. raw:: html

   <hr>

.. _accept-reject-samples-query-profiles-and-samples:

Guidelines for Searching Profiles and Samples on the Accept or Reject Web Page
-------------------------------------------------------------------------------

Navigate to the **Accept or Reject Samples** web page.

See :ref:`How to access Accept or Reject Samples web page <accessing-accept-reject-samples-web-page>` section for
guidance.

Querying using Profiles search box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the search box on the left of the **Accept or Reject Samples web page**, query the desired profile by inputting
the profile title or a substring of it. Then, press the **ENTER** key on the keyboard to perform the search for the
desired profile.

.. hint::

   The profile search box does more than just search for keywords within the profile title. It also looks for any
   samples associated with the profile that contain the search query.

   If a match is found in any of the samples, the relevant profile will be displayed in the results table.

   Other potential search queries include the value of any of the following fields:

      * name of sample co-ordinator
      * ``RACK_OR_PLATE_ID``
      * ``SPECIMEN_ID``
      * ``TUBE_OR_WELL_ID``
      * ``biosampleAccession``
      * ``public_name``
      * ``sraAccession``

.. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_profiles_table_search_box.png
   :alt: Profiles table search box on 'Accept or Reject Samples' web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_profiles_table_search_box.png
   :class: with-shadow with-border

   **Accept or Reject Samples web page: Profiles table search box**

.. raw:: html

   <br>

Querying using Samples search box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the search box on the right of the **Accept or Reject Samples web page**, query sample metadata then, press the
**ENTER** key on the keyboard to perform the search.

If a match is found in any of the sample records, the relevant sample(s) will be displayed in the **Samples** table.

.. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_table_search_box.png
   :alt: Samples table search box on 'Accept or Reject Samples' web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_table_search_box.png
   :class: with-shadow with-border

   **Accept or Reject Samples web page: Samples table search box**

.. raw:: html

   <hr>

.. _accept-reject-samples-within-several-manifest-groups:

Guidelines for Sample Managers Assigned to Multiple Manifest Groups
---------------------------------------------------------------------

.. note::

   The manifest dropdown menu will only be displayed on the **Accept or Reject samples** web page if you as a
   sample manager, belongs to more than one sample manager manifest group.


If you have been granted permission to be a sample manager for more than one manifest group, you can accept or reject
samples for more than one manifest group by following the steps below:

#. Click the dropdown menu displayed beside the **Choose to Accept or Reject** web page title on the left side of the
   **Accept or Reject Samples** web page as shown below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_manifest_dropdown_menu1.png
      :alt: 'Accept or Reject Samples' manifest dropdown menu is shown if sample manager belongs to more than one manifest group
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_manifest_dropdown_menu1.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Manifest dropdown menu beside 'Choose to Accept or Reject' web page title**

   .. raw:: html

      <br>

#. A list of all the manifest groups that you have been assigned to is then displayed.

   Choose the desired manifest group from the dropdown menu as shown below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_manifest_dropdown_menu2.png
      :alt: 'Accept or Reject Samples' manifest dropdown menu options are shown after the dropdown menu is clicked
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_manifest_dropdown_menu2.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Manifest dropdown menu with options displayed**

   .. raw:: html

      <br>

#. To **accept** samples, see the :ref:`accepting-samples` section

   .. centered:: **OR**

   To **reject** samples, see the :ref:`rejecting-samples` section


   .. raw:: html

      <br>

.. raw:: html

  <hr>

.. _accept-reject-samples:


Accepting or Rejecting Samples
--------------------------------

Profiles are displayed according to the associated profile type group that you have been assigned to as a sample
manager.

You can check which associated profile type a sample is associated with, by clicking the desired profile on
the left of the web page in the **Profiles** tab on the **Accept or Reject Samples** web page then, checking the
**Associated TOL (Tree of Life) Project** column for any sample record in the **Samples** table displayed (if the
profile has submitted samples) as shown below:

.. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_associated_tol_project1.png
   :alt: Associated TOL Project column in the 'Samples' table on the 'Accept or Reject Samples' web page for a single associated profile type
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_associated_tol_project1.png
   :class: with-shadow with-border
   :height: 200px

   **Sample records associated with a single associated Tree of Life (ToL) project type**

.. raw:: html

   <br>

.. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_associated_tol_project2.png
   :alt: Associated TOL Project column in the 'Samples' table on the 'Accept or Reject Samples' web page with multiple associated profile types
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_associated_tol_project2.png
   :class: with-shadow with-border
   :height: 200px

   **Sample records associated with multiple associated Tree of Life (ToL) project types**

.. note::

   A **Samples** table record will only be displayed if the desired profile that is clicked/highlighted on the left of
   the web page has submitted samples.

.. hint::

   * See :ref:`Accept or Reject Samples for more than one manifest group <accept-reject-samples-within-several-manifest-groups>`
     section for guidance if you are assigned to more than one manifest group and would like to accept or reject samples.

.. seealso::

    * :ref:`List of associated profile types (i.e. secondary projects) brokered through COPO <copo-project-associated-projects>`

.. raw:: html

  <hr>

.. _accepting-samples:

Accepting samples
~~~~~~~~~~~~~~~~~

.. note::

   If you have already accepted samples but the samples are still displayed in the **Pending Samples** tab, it is likely
   that the samples are associated with another profile type group and is pending action by another sample manager.

   See :ref:`Samples awaiting another review <faq-sample-managers-samples-awaiting-another-review>`
   :abbr:`FAQ (Frequently Asked Question)` for additional information.

#. Choose a desired profile on the left of the **Accept or Reject Samples** web page from the **Profiles** tab

#. In the **Pending Samples** tab, select desired sample record(s) by clicking the checkbox(es) associated with the
   sample record(s) (if the selected profile has samples).

   Then, click the |accept-samples-button| button as shown in the examples below.

   .. raw:: html

      <br>

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_accept_samples_button_dtol.png
      :alt: Accepting samples on the 'Accept or Reject Samples' web page for DTOL profiles
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_accept_samples_button_dtol.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Accepting samples within DTOL profiles**

   .. raw:: html

      <br>

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_accept_samples_button_erga.png
      :alt: Accepting samples on the 'Accept or Reject Samples' web page for ERGA profiles
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_accept_samples_button_erga.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Accepting samples within ERGA profiles**

   .. raw:: html

      <br>

   A confirmation popup dialog will be displayed as shown below after the |accept-samples-button| button is clicked.

   Click the **Okay** button to accept the selected sample record(s) or click the **Cancel** button to cancel the
   action.

   .. figure:: /assets/images/samples/accept_reject_samples/modals/samples_accept_reject_accept_samples_confirmation_popup_dialog.png
      :alt: Accept samples confirmation dialog on the 'Accept or Reject Samples' web page
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/modals/samples_accept_reject_accept_samples_confirmation_popup_dialog.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Accept samples confirmation dialog**


   .. raw:: html

      <br>

#. If the **Okay** button is clicked, the accepted samples will proceed to the processing stage and will be displayed
   in the **Processing Samples** tab as shown in the examples below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_processing_stage_asg_dtol.png
      :alt: Accepted ASG or DTOL samples at the 'Processing Samples' stage on the 'Accept or Reject Samples' web page
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_processing_stage_asg_dtol.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Accepted DTOL samples at the processing stage**

   .. raw:: html

      <br>

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_processing_stage_erga.png
      :alt: Accepted samples at the 'Processing Samples' stage on the 'Accept or Reject Samples' web page
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_processing_stage_erga.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Accepted ERGA samples at the processing stage**

   .. raw:: html

      <br>

#. After the samples have been processed, the samples will proceed to the accepted stage and will be displayed in the
   **Accepted Samples** tab as shown the examples below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_accepted_stage_asg_dtol.png
      :alt: Accepted samples at the 'Accepted Samples' stage on the 'Accept or Reject Samples' web page
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_accepted_stage_asg_dtol.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Accepted DTOL samples at the accepted stage**

   .. raw:: html

      <br>

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_accepted_stage_erga.png
      :alt: Accepted ERGA samples at the 'Accepted Samples' stage on the 'Accept or Reject Samples' web page
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_accepted_samples_at_accepted_stage_erga.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Accepted ERGA samples at the accepted stage**

.. raw:: html

  <hr>

.. _rejecting-samples:

Rejecting samples
~~~~~~~~~~~~~~~~~

#. Choose desired profile on the left of the **Accept or Reject Samples** web page from the **Profiles** tab

#. In the **Pending Samples** tab, select desired sample record(s) by clicking the checkbox(es) associated with the
   sample record(s).

   Then, click the |reject-samples-button| button as shown below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_reject_samples_button.png
      :alt: Rejecting samples on the 'Accept or Reject Samples' web page
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_reject_samples_button.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Rejecting samples**

   .. raw:: html

      <br>

#. The samples will proceed to the rejected stage and will be displayed in the **Rejected Samples** tab as shown below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_rejected_samples_at_rejected_stage.png
      :alt: Rejected samples at the 'Rejected Samples' stage on the 'Accept or Reject Samples' web page
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_rejected_samples_at_rejected_stage.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Rejected samples at the rejected stage**

.. raw:: html

   <hr>

.. _samples-submission-download-sample-manifest-sample-managers:

Download Submitted Sample Manifests
------------------------------------

As a **sample manager**, you can download submitted (filled) manifests by following the steps below:

#. Navigate to the **Accept or Reject Samples** web page.

   See :ref:`How to access Accept or Reject Samples web page <accessing-accept-reject-samples-web-page>` section for
   guidance.

#. On the left of the **Accept or Reject Samples** web page, click the |link-icon| icon in the **Samples Link** table
   column of the **Profiles** table row for the profile that you would like upload a manifest for or update a submitted
   manifest for as shown below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_dtol_profile.png
      :alt: Pointer to 'Samples' web page link on the 'Accept or Reject Samples' web page for the desired DTOL profile
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_dtol_profile.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Navigate to 'Samples' web page by clicking the link associated with a DTOL profile**

   .. raw:: html

            <br>

   .. centered:: **OR**

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_erga_profile.png
      :alt: Pointer to 'Samples' web page link on the 'Accept or Reject Samples' web page for the desired ERGA profile
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_erga_profile.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Navigate to 'Samples' web page by clicking the link associated with an ERGA profile**

   .. raw:: html

      <br>

#. The **Samples** web page will be displayed as shown below:

    .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_dtol.png
        :alt: Pointer to 'Samples' web page on the 'Accept or Reject Samples' web page for a DTOL profile
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_dtol.png
        :class: with-shadow with-border

        **Samples web page for a DTOL profile**

    .. raw:: html

       <br>


    .. centered:: **OR**

    .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_erga.png
        :alt: Pointer to 'Samples' web page on the 'Accept or Reject Samples' web page for an ERGA profile
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_erga.png
        :class: with-shadow with-border

        **Samples web page for an ERGA profile**

   .. raw:: html

      <br>

#. Download the submitted manifest by following the guidelines described in the
   :ref:`downloading-submitted-sample-manifest` section

.. raw:: html

   <hr>

.. _permits-submission-download-permits-sample-managers:

Download Submitted Permits
----------------------------

If you have been assigned as a **sample manager**, you can view the permits submitted for submitted sample(s) on the
`Accept/Reject Samples' web page <https://copo-project.org/copo/dtol_submission/accept_reject_sample>`__ by following the
steps below:

.. note::

   * Permits can only be downloaded for submitted samples that are **pending** action by a sample manager or have been
     **accepted** by a sample manager.

   * Permits exist for :abbr:`ERGA (European Reference Genome Atlas)` [#f3]_ profiles only.

.. hint::

   To download submitted permits for samples within the **Accepted Samples** tab, ``CTRL + Click`` the desired sample
   record(s) then, click the |download-permits-button2| button to download permit(s) submitted for the selected
   record(s).


#. Navigate to the **Accept or Reject Samples** web page.

   See :ref:`How to access Accept or Reject Samples web page <accessing-accept-reject-samples-web-page>` section for
   guidance on how to access the **Accept or Reject Samples** web page.

#. Select the sample record(s) that you would like to download the permits for.

   Then, click the |download-permits-button2| button to download permit(s) submitted for the selected sample record(s).

#. If any permit submission(s) exist for the selected sample record(s), the permits will be automatically downloaded for
   the selected sample record(s).

   .. hint::

      Permits are downloaded as a ``.zip`` file

   If no permits were submitted for the selected sample record(s), a message is displayed in the popup
   dialog indicating such as shown below:

   .. figure:: /assets/images/samples/accept_reject_samples/modals/samples_accept_reject_download_permits_dialog_with_no_permits_exist_message.png
      :alt: No permits exist message in popup dialog for selected sample record(s)
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/modals/samples_accept_reject_download_permits_dialog_with_no_permits_exist_message.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Popup dialog displaying message, 'No permits exist for selected sample record(s)'**


.. raw:: html

   <hr>

.. _image-submission-view-images-sample-managers:

View Submitted Images
----------------------

If you have been assigned as a **sample manager**, you can view the images submitted for submitted sample(s) on the
`Accept/Reject Samples' web page <https://copo-project.org/copo/dtol_submission/accept_reject_sample>`__ by following the
steps below:

.. hint::

   To view submitted images for samples within the **Accepted Samples** tab, ``CTRL + Click`` the desired sample
   record(s) then, click the |view-images-button2| button to view image(s) submitted for the selected record(s).

#. Navigate to the **Accept or Reject Samples** web page.

   See :ref:`How to access Accept or Reject Samples web page <accessing-accept-reject-samples-web-page>` section for
   guidance on how to access the **Accept or Reject Samples** web page.

#. Select the sample record(s) that you would like to view images for.

   Then, click the |view-images-button2| button to view image(s) submitted for the selected sample record(s).

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_view_images_button.png
     :alt: 'Accept or Reject Samples' web page
     :align: center
     :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_view_images_button.png
     :class: with-shadow with-border

     **Accept or Reject Samples web page: Pointer to 'View images' button**

   .. raw:: html

      <br>

#. If any image submission(s) exist for the selected sample record(s), a popup dialog will be displayed with the
   image(s) submitted for the selected sample record(s) as shown below:

   .. hint::

      Click the image to view a larger version.

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_view_images_dialog_with_images_displayed.png
      :alt: View images popup dialog with images displayed for selected sample record(s)
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_view_images_dialog_with_images_displayed.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Popup dialog displaying submitted image(s) for selected sample record(s)**

   .. raw:: html

      <br>

   .. centered:: **OR**

   If no images were submitted for the selected sample record(s), a message is displayed in the popup
   dialog indicating such as shown below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_view_images_dialog_with_no_images_exist_message.png
      :alt: No images exists message in popup dialog for selected sample record(s)
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_view_images_dialog_with_no_images_exist_message.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Popup dialog displaying message, 'No images exist for selected sample record(s)'**

.. raw:: html

   <hr>

Upload Manifest or Update Submitted Manifest on behalf of Manifest Submitters
-----------------------------------------------------------------------------

.. note::

  * The manifest dropdown menu will only be displayed on the **Accept or Reject samples** web page if you as a
    sample manager, belongs to more than one sample manager manifest group.

  * The **Samples** table will only be displayed if the selected/highlighted profile has submitted samples.

.. hint::

   * **All** sample field values can be updated by sample managers.

   * **Some** sample field values can be updated by sample providers. See the :ref:`samples-update` section for
     information about which field values can be updated by sample providers.

   * Samples can be updated by resubmitting the manifest with the updated metadata.

The following steps can be followed to upload a manifest or update a submitted manifest on behalf of a manifest
submitter [#f2]_:

#. Navigate to the **Accept or Reject Samples** web page.

   See :ref:`How to access Accept or Reject Samples web page <accessing-accept-reject-samples-web-page>` section for
   guidance.

#. Search for the profile that you would like to upload a manifest for or update a submitted manifest for.

   See :ref:`accept-reject-samples-query-profiles-and-samples` section for guidance on how to query profiles and
   samples on the **Accept or Reject Samples** web page.

#. On the left of the **Accept or Reject Samples web page**, click the |link-icon| icon in the **Samples Link** table
   column of the **Profiles** table row for the profile that you would like upload a manifest for or update a submitted
   manifest for as shown in the examples below:

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_dtol_profile.png
      :alt: Pointer to 'Samples' web page link on the 'Accept or Reject Samples' web page for the desired DTOL profile
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_dtol_profile.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Navigate to 'Samples' web page by clicking the link associated with a DTOL profile**

   .. raw:: html

            <br>

   .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_erga_profile.png
      :alt: Pointer to 'Samples' web page link on the 'Accept or Reject Samples' web page for the desired ERGA profile
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_accept_reject_pointer_to_samples_link_icon_for_erga_profile.png
      :class: with-shadow with-border

      **Accept or Reject Samples web page: Navigate to 'Samples' web page by clicking the link associated with an ERGA profile**

   .. raw:: html

      <br>

#. The **Samples** web page will be displayed as shown in the examples below:

    .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_dtol.png
        :alt: Pointer to 'Samples' web page on the 'Accept or Reject Samples' web page for a DTOL profile
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_dtol.png
        :class: with-shadow with-border

        **Samples web page for a DTOL profile**

    .. raw:: html

       <br>

    .. figure:: /assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_erga.png
        :alt: Pointer to 'Samples' web page on the 'Accept or Reject Samples' web page for an ERGA profile
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/accept_reject_samples/ui/samples_web_page_after_clicked_link_icon_erga.png
        :class: with-shadow with-border

        **Samples web page for an ERGA profile**

   .. raw:: html

      <br>

#. If you do not have the submitted manifest for the profile, see the :ref:`downloading-submitted-sample-manifest`
   section for guidance on how to download the submitted sample manifest. Then, refer to the :ref:`samples-update`
   section for guidance on how to submit the modified manifest.

   .. centered:: **OR**

   If you have the submitted manifest for the profile, see the :ref:`samples-update` section for guidance on how to
   update the submitted manifest.

   .. centered:: **OR**

   If you would like to upload a newer version of a manifest that has already been submitted on behalf of the
   manifest provider, please follow the steps below:

   #. Download the submitted manifest by following the guidelines described in the
      :ref:`downloading-submitted-sample-manifest` section if you do not have the newer version of the manifest with
      the sample metadata information.

   #. Transfer the sample metadata from the submitted manifest into the newer version of the manifest.

   #. Send an email to the COPO team at :email:`ei.copo@earlham.ac.uk <ei.copo@earlham.ac.uk>`, indicating the profile
      type as well as the profile title and requesting that the samples be **removed** from the profile.

      The samples has to be removed from the profile so that the sample metadata in the newer version of the manifest
      can be registered in the profile.

      .. important::

         Please request that the samples be removed from the profile **only** if you are certain and have the newer
         version of the manifest with the sample metadata information.

         The samples **cannot** be restored after they have been removed from the profile.

   #. Upload the newer version of the manifest by referring to the guidelines described in the desired link below to
      learn more about each type of manifest submission:

      * :ref:`Aquatic Symbiosis Genomics (ASG) manifest submission<submit-manifest-asg>`
      * :ref:`Darwin Tree of Life (DToL) manifest submission <submit-manifest-dtol>`
      * :ref:`Darwin Tree of Life Environmental (DToL_ENV) manifest submission <dtol-env-manifest-submissions>`
      * :ref:`European Reference Genome Atlas (ERGA) manifest submission <submit-manifest-erga>`

   .. hint::

      See :ref:`download-manifest-templates` section for information about downloading manifest templates.

.. raw:: html

   <hr>


.. rubric:: Footnotes

.. [#f1] See term: :term:`Sample manager`
.. [#f2] See term: :term:`Sample submitter`. Sample submitter may also be referred to as a
         manifest provider or manifest submitter.
.. [#f3] See term: :term:`ERGA`.


..
    Images declaration
..

.. |accept-samples-button| image:: /assets/images/samples/accept_reject_samples/buttons/samples_accept_reject_button_accept.png
   :height: 4ex
   :class: no-scaled-link

.. |accept-reject-samples-navigation-button| image:: /assets/images/samples/accept_reject_samples/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-permits-button2| image:: /assets/images/buttons/permits_download_button2.png
   :height: 4ex
   :class: no-scaled-link

.. |reject-samples-button| image:: /assets/images/samples/accept_reject_samples/buttons/samples_accept_reject_button_reject.png
   :height: 4ex
   :class: no-scaled-link

.. |link-icon| image:: /assets/images/samples/accept_reject_samples/icons/samples_accept_reject_samples_link_icon.png
   :height: 3ex
   :class: no-scaled-link

.. |view-images-button2| image:: /assets/images/buttons/images_view_button2.png
   :height: 4ex
   :class: no-scaled-link