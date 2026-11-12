---
title: "FacesRemoved Property (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "FacesRemoved"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~FacesRemoved.html"
---

# FacesRemoved Property (IShellFeatureData)

Gets the faces removed and sets the faces to remove in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FacesRemoved As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim value As System.Object

instance.FacesRemoved = value

value = instance.FacesRemoved
```

### C#

```csharp
System.object FacesRemoved {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FacesRemoved {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of removed [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [ShellFeatureData::FacesRemoved](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~FacesRemoved.html).

## Examples

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::IGetFacesRemoved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetFacesRemoved.html)
[IShellFeatureData::ISetFacesRemoved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetFacesRemoved.html)
[IShellFeatureData::FacesRemovedCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~FacesRemovedCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
