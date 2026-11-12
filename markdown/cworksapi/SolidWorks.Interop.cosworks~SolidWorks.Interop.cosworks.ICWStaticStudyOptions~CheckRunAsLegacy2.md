---
title: "CheckRunAsLegacy2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "CheckRunAsLegacy2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckRunAsLegacy2.html"
---

# CheckRunAsLegacy2 Property (ICWStaticStudyOptions)

Gets or sets whether to run as legacy and import only the normal component of the pressure load from a SOLIDWORKS Flow Simulation results file.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckRunAsLegacy2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.CheckRunAsLegacy2 = value

value = instance.CheckRunAsLegacy2
```

### C#

```csharp
System.bool CheckRunAsLegacy2 {get; set;}
```

### C++/CLI

```cpp
property System.bool CheckRunAsLegacy2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to run as legacy and import only the normal component of the pressure load, 0 or false to import all components including shear stress (see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::CheckRunAsLegacy2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~CheckRunAsLegacy2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
