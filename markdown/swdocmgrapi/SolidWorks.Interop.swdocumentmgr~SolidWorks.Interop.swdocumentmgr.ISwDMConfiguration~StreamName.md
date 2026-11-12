---
title: "StreamName Property (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "StreamName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~StreamName.html"
---

# StreamName Property (ISwDMConfiguration)

Gets the name of the stream for the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StreamName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim value As System.String

value = instance.StreamName
```

### C#

```csharp
System.string StreamName {get;}
```

### C++/CLI

```cpp
property System.String^ StreamName {
   System.String^ get();
}
```

### Property Value

Name of the stream for the configuration

## VBA Syntax

See [SwDMConfiguration::StreamName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~StreamName.html).

## Examples

[Write Parasolid Partition Stream to File (C#)](Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (VB.NET)](Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm)

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
