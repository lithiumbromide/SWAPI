---
title: "GetCoordinateType Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "GetCoordinateType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetCoordinateType.html"
---

# GetCoordinateType Method (ICWRestraint)

Gets the coordinate system type for this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinateType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim value As System.Integer

value = instance.GetCoordinateType()
```

### C#

```csharp
System.int GetCoordinateType()
```

### C++/CLI

```cpp
System.int GetCoordinateType();
```

### Return Value

Coordinate system type as defined in [swsCoordinateType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsCoordinateType_e.html)

## VBA Syntax

See [CWRestraint::GetCoordinateType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~GetCoordinateType.html).

## Examples

See the [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html) examples.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
