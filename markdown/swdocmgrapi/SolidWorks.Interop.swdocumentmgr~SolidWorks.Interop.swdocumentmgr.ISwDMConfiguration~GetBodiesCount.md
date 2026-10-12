---
title: "GetBodiesCount Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "GetBodiesCount"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBodiesCount.html"
---

# GetBodiesCount Method (ISwDMConfiguration)

Gets the number of solid bodies for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim value As System.Integer

value = instance.GetBodiesCount()
```

### C#

```csharp
System.int GetBodiesCount()
```

### C++/CLI

```cpp
System.int GetBodiesCount();
```

### Return Value

Number of solid bodies

## VBA Syntax

See [SwDMConfiguration::GetBodiesCount](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~GetBodiesCount.html).

## Examples

[Write Parasolid Partition Stream to File (C#)](Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (VB.NET)](Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm)

## Remarks

This method only returns the number of solid bodies for documents saved in SOLIDWORKS 2003 and lower. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

Call this method before calling [ISwDMConfiguration::GetBody](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.html) to find out the number of solid bodies for this configuration.

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)
[ISwDMConfiguration3::GetImportedBodiesCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBodiesCount.html)
[ISwDMConfiguration3::GetImportedBody Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBody.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
