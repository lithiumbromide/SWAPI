---
title: "LibraryPart Property (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "LibraryPart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LibraryPart.html"
---

# LibraryPart Property (ILibraryFeatureData)

Gets the path and filename of the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LibraryPart As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim value As System.String

value = instance.LibraryPart
```

### C#

```csharp
System.string LibraryPart {get;}
```

### C++/CLI

```cpp
property System.String^ LibraryPart {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and filename of the library feature

## VBA Syntax

See [LibraryFeatureData::LibraryPart](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~LibraryPart.html).

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize.html)
[ILibraryFeatureData::LinkToLibraryPart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LinkToLibraryPart.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
