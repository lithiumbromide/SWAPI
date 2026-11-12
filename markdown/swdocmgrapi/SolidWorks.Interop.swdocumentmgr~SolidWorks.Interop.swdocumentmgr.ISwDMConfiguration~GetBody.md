---
title: "GetBody Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "GetBody"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.html"
---

# GetBody Method (ISwDMConfiguration)

Gets the body at the specified index in the specified Parasolid binary file (filename extension .x_b).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBody( _
   ByVal index As System.Integer, _
   ByVal fileName As System.String _
) As SwDmBodyError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim index As System.Integer
Dim fileName As System.String
Dim value As SwDmBodyError

value = instance.GetBody(index, fileName)
```

### C#

```csharp
SwDmBodyError GetBody(
   System.int index,
   System.string fileName
)
```

### C++/CLI

```cpp
SwDmBodyError GetBody(
   System.int index,
   System.String^ fileName
)
```

### Parameters

- `index`: Index number indicating the body to get
- `fileName`: Full path and filename in which to get the body

### Return Value

Success or error code as defined by [SwDmBodyError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmBodyError.html)

## VBA Syntax

See [SwDMConfiguration::GetBody](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~GetBody.html).

## Examples

[Write Parasolid Partition Stream to File (C#)](Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (VB.NET)](Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm)

## Remarks

This method supports:

- part and assembly documents saved in SOLIDWORKS 2003 and earlier.
- only assembly documents saved in SOLIDWORKS 2004 and later. Use [ISwDMConfiguration2::GetPartitionStream](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration2~GetPartitionStream.html) for part documents saved in SOLIDWORKS 2004 and later.

To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

To find out the number of solid bodies in this Parasolid binary file, call [ISwDMConfiguration::GetBodiesCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~GetBodiesCount.html) before calling this method.

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)
[ISwDMConfiguration3::GetImportedBodiesCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBodiesCount.html)
[ISwDMConfiguration3::GetImportedBody Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBody.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
