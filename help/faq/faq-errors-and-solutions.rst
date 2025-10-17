.. _faq-errors-and-solutions:

Errors & Solutions
--------------------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`, click the arrow icon
   (|collapsible-item-arrow|) below any question to expand or collapse it.

.. raw:: html

  <hr>

.. _faq-errors-invalid-date-format:

Invalid date in column
~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. hint::

      As regards to date formats, ``YYYY`` represents the four-digit year, ``MM`` is the two-digit month and ``DD``
      is the two-digit day.

   This error can pertain to any date column such as **collection date** or **DATE_OF_COLLECTION** depending on the
   type of manifest that you are trying to upload.

   Two main reasons why this error occurs are:

   .. _faq-errors-invalid-date-entered:

   #. **Invalid date format**: The date provided does not match a valid date format.

      *   Depending on the column, valid date formats may include options such as ``YYYY-MM-DD``, ``YYYY-MM``, ``YYYY``,
          ``NOT_COLLECTED`` or ``NOT_PROVIDED``. The error message shown will display the valid options for the specific
          column.

      *  A date-time value is provided but with a space separator (e.g. ``2025-05-01 14:30:00``) instead of a
         a date-time format with a **T** separator (e.g. ``2025-05-01T14:30:00``).

      .. raw:: html

         <br>

      .. _faq-errors-invalid-date-format-time-added:

   #. **Valid date only value but time being added**: A valid date is provided but the spreadsheet internally and
      automatically converts **date only** values to date-time values where the time component is set to ``00:00:00``.

      This time component is usually not visible in the cell. An example of this is ``2025-05-01 00:00:00``) but only
      ``2025-05-01`` is inputted and visible in the cell.

      Refer to the :ref:`Solution option #2 <faq-errors-invalid-date-format-time-added-solution-2>` below to resolve
      this issue.

      .. raw:: html

         <br>

      .. figure:: /assets/images/errors/error_invalid_collection_date.png
         :alt: Example of invalid date format error message for collection date column
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/errors/error_invalid_collection_date.png
         :class: with-shadow with-border
         :height: 200px

         **Example of invalid date format error message for collection date column**

      .. raw:: html

         <br>

      .. figure:: /assets/images/errors/error_invalid_date_of_collection.png
         :alt: Example of invalid date format error message for DATE_OF_COLLECTION column
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/errors/error_invalid_date_of_collectione.png
         :class: with-shadow with-border
         :height: 200px

         **Example of invalid date error message for DATE_OF_COLLECTION column**

   **Solutions**

    **Option 1**: Re-format the date column in the spreadsheet

      #.	Select the entire column with the date values to be corrected.
      #.	Right-click then, select **Format Cells...**
      #.	Select **Custom**
      #.	In the **Type** field, enter ``yyyy-mm-dd``
      #.	Click **OK**
      #.	Save the spreadsheet and reupload the file.

      If the error persists, try the alternative solution below.

    .. centered:: **OR**

    .. _faq-errors-invalid-date-format-time-added-solution-2:

    **Option 2**: Convert date cell to text using a formula in a temporary column

      #. In a new column, enter ``=TEXT(A1,"yyyy-mm-dd")`` (replace ``A1`` with the cell you want to convert).
      #. Copy the formula results.
      #. Use **Paste Values** or **Paste Special** --> **Values** to overwrite the original column with the formatted
         text.
      #. Delete the temporary column.
      #. Save the spreadsheet and reupload the file.


.. raw:: html

  <hr>

.. _faq-errors-invalid-column:

Invalid column '<column-name>'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   This error occurs when a column header in the uploaded manifest does not match any of the expected column headers
   for the selected checklist.

   This error usually occurs when the incorrect checklist is selected or if there is a typo in the


   .. figure:: /assets/images/errors/error_invalid_column_incorrect_manifest_uploaded.png
      :alt: Example of incorrect manifest uploaded error message
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/errors/error_invalid_column_incorrect_manifest_uploaded.png
      :class: with-shadow with-border
      :height: 300px

      **Example of incorrect manifest uploaded error message**

   **Solutions**

    Verify that the correct checklist is selected from the dropdown menu then, re-upload a manifest that matches the
    selected checklist.

    Alternatively, verify that the column header is spelt correctly and matches one of the expected column headers
    for the selected checklist. Refer to the :ref:`manifest-checklist` section for guidance.

.. raw:: html

   <br><hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link