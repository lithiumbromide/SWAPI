---
title: "PartitionStreamName Property (ISwDMConfiguration2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration2"
member: "PartitionStreamName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~PartitionStreamName.html"
---

# PartitionStreamName Property (ISwDMConfiguration2)

Gets the name of the Parasolid body partition stream.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PartitionStreamName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration2
Dim value As System.String

value = instance.PartitionStreamName
```

### C#

```csharp
System.string PartitionStreamName {get;}
```

### C++/CLI

```cpp
property System.String^ PartitionStreamName {
   System.String^ get();
}
```

### Property Value

Name of the stream; valid filename extensions are *.xmp_bin for NTFS and *.p_b for FAT

## VBA Syntax

See [SwDMConfiguration2::PartitionStreamName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration2~PartitionStreamName.html).

## Remarks

Call this method before calling [ISwDMConfiguration2::GetPartitionStream](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration2~GetPartitionStream.html).

## See Also

[ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.html)
[ISwDMConfiguration2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
