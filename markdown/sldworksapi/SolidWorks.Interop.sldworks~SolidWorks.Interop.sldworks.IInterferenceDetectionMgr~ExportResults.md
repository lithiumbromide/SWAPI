---
title: "ExportResults Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "ExportResults"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ExportResults.html"
---

# ExportResults Method (IInterferenceDetectionMgr)

Saves interference detection results to a file.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportResults( _
   ByVal FileName As System.String, _
   ByVal IncludeThumbnail As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim FileName As System.String
Dim IncludeThumbnail As System.Boolean
Dim value As System.Boolean

value = instance.ExportResults(FileName, IncludeThumbnail)
```

### C#

```csharp
System.bool ExportResults(
   System.string FileName,
   System.bool IncludeThumbnail
)
```

### C++/CLI

```cpp
System.bool ExportResults(
   System.String^ FileName,
   System.bool IncludeThumbnail
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path name of the file (***.xlsx** or ***.csv**) (see **Remarks**)
- `IncludeThumbnail`: True to include thumbnail images of interfering components in the Microsoft Excel results, false to not (see **Remarks**)

### Return Value

True if the export is successful, false if not

## VBA Syntax

See [InterferenceDetectionMgr::ExportResults](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~ExportResults.html).

## Examples

[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)

## Remarks

This method corresponds to the **Save Results** button in the Interference Detection PropertyManager.

Filename is a Microsoft Excel file or a ***.csv** file that contains the information presented in the Results list box of the Interference Detection PropertyManager:

| A | B | C | D | E | F | G |
| --- | --- | --- | --- | --- | --- | --- |
| Interference ID | Interference Preview | Interference volume (mm^3) | Component 1 name | Component 2 name | Component 1 full reference | Component 2 full reference |

IncludeThumbnail is only valid if Filename is a Microsoft Excel file.

If IncludeThumbnail is true, then:

- A thumbnail is created in each row of Column B (Interference Preview).
- Each thumbnail has:

  - 128X128 pixel resolution
  - White background
  - Isometric orientation

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
