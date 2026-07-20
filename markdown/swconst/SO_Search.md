---
title: "System Options > Search"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Search.htm"
---

# System Options > Search

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture corresponds to the settings on that dialog.
- titled

  [Obsolete
  Enumerators](#Obsolete)

  contains enumerators that previously appeared on the

  dialog
  but are now obsolete.

The Search dialog is not available in SOLIDWORKS Connected.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Show SOLIDWORKS search box | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSearchShowSOLIDWORKSSearchBox) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSearchShowSOLIDWORKSSearchBox,
< OnFlag >) | Boolean value | Specifies whether to show the SOLIDWORKS search box |
| File and Model Search - Search while typing (incremental search) (Not
supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSearchWhileTyping) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSearchWhileTyping,
< OnFlag >) | Boolean value | Specifies whether to start the search while typing the search string |
| File and Model Search - Results per page (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSearchResultsPerPage) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSearchResultsPerPage,
< Value >) | Integer value | Specifies number of search results to show per page |
| File and Model Search - Maximum results per data source (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSearchMaxResultsPerDataSource) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSearchMaxResultsPerDataSource,
< Value >) | Integer value | Specifies maximum number of results per data source |
| File and Model Search - Indexing Performance (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSearchIndexingPerformance) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSearchIndexingPerformance,
swSearchIndexingPerformance_e.< Value >) | See swSearchIndexingPerformance_e for valid options | Specifies when to perform search indexing |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Comment |
| --- | --- |
| swSearchDissectionScheduleDaily | Obsolete |
| swSearchDissectionDailyStartTime | Obsolete |
| swSearchDissectionDailyStopTime | Obsolete |
| swSearchDissectionLocation | Obsolete |
| swSearchIncludeContentCentral | Obsolete |
