---
title: "GetPartitionStream Method (ISwDMConfiguration2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration2"
member: "GetPartitionStream"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetPartitionStream.html"
---

# GetPartitionStream Method (ISwDMConfiguration2)

Gets the Parasolid partition stream that has the body partition information and writes it the specified file. Supports part documents only.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartitionStream( _
   ByVal fileName As System.String _
) As SwDmBodyError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration2
Dim fileName As System.String
Dim value As SwDmBodyError

value = instance.GetPartitionStream(fileName)
```

### C#

```csharp
SwDmBodyError GetPartitionStream(
   System.string fileName
)
```

### C++/CLI

```cpp
SwDmBodyError GetPartitionStream(
   System.String^ fileName
)
```

### Parameters

- `fileName`: Filename to which to write the Parasolid partition and body information (see Remarks)

### Return Value

Success or error code as defined by [SwDmBodyError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmBodyError.html)

## VBA Syntax

See [SwDMConfiguration2::GetPartitionStream](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration2~GetPartitionStream.html).

## Examples

[Write Parasolid Partition Stream to File (C#)](Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (VB.NET)](Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm)
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)

## Remarks

This method only supports part documents saved in SOLIDWORKS 2004 and later. Use [ISwDMConfiguration::GetBody](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.html) for part dcouments saved in SOLIDWORKS 2003 and earlier and assembly documents saved in any version of SOLIDWORKS.

To get the version of a part document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

Before using this method, call [ISwDMConfiguration2::PartitionStreamName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration2~PartitionStreamName.html) to get fileName. Valid filename extensions are *.xmp_bin for NTFS and *.p_b for FAT.

| If fileName... | Then... |
| --- | --- |
| Does not exit | This method creates the file and writes the Parasolid partition and body information to that file |
| Exists | Writes the Parasolid partition and body information to that file, overwriting any data in that file |

## See Also

[ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.html)
[ISwDMConfiguration2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
