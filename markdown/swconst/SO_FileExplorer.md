---
title: "System Options > File Explorer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_FileExplorer.htm"
---

# System Options > File Explorer

The File Explorer settings are not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Show in File Explorer view - My Documents | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowMyDocuments) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowMyDocuments, < OnFlag >) | Boolean value | Specifies whether to show My Documents folder in SOLIDWORKS File Explorer |
| Show in File Explorer view - My Computer | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowMyComputer) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowMyComputer, < OnFlag >) | Boolean value | Specifies whether to show My Computer folder in SOLIDWORKS File Explorer |
| Show in File Explorer view - My Network Places | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowMyNetworkPlaces) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowMyNetworkPlaces, < OnFlag >) | Boolean value | Specifies whether to show My Documents folder in SOLIDWORKS File Explorer |
| Show in File Explorer view - Recent Documents | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowRecentDocuments) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowRecentDocuments, < OnFlag >) | Boolean value | Specifies whether to show My Documents folder in SOLIDWORKS File Explorer |
| Show in File Explorer view - Hidden referenced documents | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowHiddenReferencedDocuments) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowHiddenReferencedDocuments, < OnFlag >) | Boolean value | Specifies whether to show assembly components that are in memory, but are not open, in the Open in SOLIDWORKS folder in SOLIDWORKS File Explorer |
| Show in File Explorer view - Samples | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowSamples) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFileExplorerShowSamples, < OnFlag >) | Boolean value | Specifies whether to show the Sample folders, which contains online tutorial and What's New sample files, in SOLIDWORKS File Explorer |
