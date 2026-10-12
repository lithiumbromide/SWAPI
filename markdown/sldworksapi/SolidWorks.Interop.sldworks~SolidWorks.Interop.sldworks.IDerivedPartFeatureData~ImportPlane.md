---
title: "ImportPlane Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportPlane.html"
---

# ImportPlane Property (IDerivedPartFeatureData)

Gets or sets whether to import planes with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportPlane As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportPlane = value

value = instance.ImportPlane
```

### C#

```csharp
System.bool ImportPlane {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportPlane {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its planes, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportPlane](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportPlane.html).

## Examples

[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)
[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
