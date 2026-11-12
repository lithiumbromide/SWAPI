---
title: "CreatedBy Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "CreatedBy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CreatedBy.html"
---

# CreatedBy Property (IFeature)

Gets the name of the user who created the feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CreatedBy As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.String

value = instance.CreatedBy
```

### C#

```csharp
System.string CreatedBy {get;}
```

### C++/CLI

```cpp
property System.String^ CreatedBy {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the user who created the feature

## VBA Syntax

See [Feature::CreatedBy](ms-its:sldworksapivb6.chm::/sldworks~Feature~CreatedBy.html).

## Examples

[Get Names of Creators of Features (VBA)](Get_Names_of_Creators_of_Features_Example_VB.htm)
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)
[Get Names of Creators of Features (C#)](Get_Names_of_Creators_of_Features_Example_CSharp.htm)
[Get Names of Creators of Features (VB.NET)](Get_Names_of_Creators_of_Features_Example_VBNET.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::DateCreated Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateCreated.html)
[IFeature::DateModified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateModified.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
