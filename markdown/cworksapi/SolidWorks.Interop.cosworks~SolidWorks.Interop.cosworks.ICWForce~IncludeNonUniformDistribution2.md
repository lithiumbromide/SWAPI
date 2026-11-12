---
title: "IncludeNonUniformDistribution2 Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "IncludeNonUniformDistribution2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html"
---

# IncludeNonUniformDistribution2 Property (ICWForce)

Gets or sets whether to use a nonuniform distribution of this force.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeNonUniformDistribution2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Boolean

instance.IncludeNonUniformDistribution2 = value

value = instance.IncludeNonUniformDistribution2
```

### C#

```csharp
System.bool IncludeNonUniformDistribution2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeNonUniformDistribution2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true if nonuniform force distribution, 0 or false if not (see **Remarks**)

## VBA Syntax

See [CWForce::IncludeNonUniformDistribution2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~IncludeNonUniformDistribution2.html).

## Examples

[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
