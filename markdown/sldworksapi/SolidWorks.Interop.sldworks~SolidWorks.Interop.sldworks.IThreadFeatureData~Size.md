---
title: "Size Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "Size"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Size.html"
---

# Size Property (IThreadFeatureData)

Gets or sets the size of the thread of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Size As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.String

instance.Size = value

value = instance.Size
```

### C#

```csharp
System.string Size {get; set;}
```

### C++/CLI

```cpp
property System.String^ Size {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread size (see **Remarks**)

## VBA Syntax

See [ThreadFeatureData::Size](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~Size.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property corresponds to a Size selected in the Thread PropertyManager for a selected [IThreadFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Type.html).

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
