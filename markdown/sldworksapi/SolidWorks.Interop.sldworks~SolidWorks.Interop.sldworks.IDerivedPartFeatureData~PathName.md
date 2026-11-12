---
title: "PathName Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "PathName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~PathName.html"
---

# PathName Property (IDerivedPartFeatureData)

Gets the path for the derived part feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property PathName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.String

instance.PathName = value

value = instance.PathName
```

### C#

```csharp
System.string PathName {get; set;}
```

### C++/CLI

```cpp
property System.String^ PathName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fully qualified path and file name of the derived part feature

## VBA Syntax

See [DerivedPartFeatureData::PathName](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~PathName.html).

## Examples

[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)
[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
