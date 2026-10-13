---
title: "Type Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Type.html"
---

# Type Property (IThreadFeatureData)

Gets or sets the thread profile of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.String

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.string Type {get; set;}
```

### C++/CLI

```cpp
property System.String^ Type {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread profile (see **Remarks**)

## VBA Syntax

See [ThreadFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~Type.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property corresponds to a Type in the Thread PropertyManager.

Types are defined in ***.sldlfp** files. You can specify this property with or without the sldlfp extension and path. If you specify this property without:

- a path, SOLIDWORKS searches for the file in the folder specified by **Tools > Options > System Options > File Locations > Show folders for Thread Profiles**.
- an extension, SOLIDWORKS assumes the extension is sldlfp.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::Size Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Size.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
