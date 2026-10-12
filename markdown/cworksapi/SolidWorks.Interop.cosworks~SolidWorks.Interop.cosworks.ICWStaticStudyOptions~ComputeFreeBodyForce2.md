---
title: "ComputeFreeBodyForce2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ComputeFreeBodyForce2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ComputeFreeBodyForce2.html"
---

# ComputeFreeBodyForce2 Property (ICWStaticStudyOptions)

Gets or sets whether to prepare the grid force balance at every node.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComputeFreeBodyForce2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.ComputeFreeBodyForce2 = value

value = instance.ComputeFreeBodyForce2
```

### C#

```csharp
System.bool ComputeFreeBodyForce2 {get; set;}
```

### C++/CLI

```cpp
property System.bool ComputeFreeBodyForce2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to compute free body forces, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::ComputeFreeBodyForce2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ComputeFreeBodyForce2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
