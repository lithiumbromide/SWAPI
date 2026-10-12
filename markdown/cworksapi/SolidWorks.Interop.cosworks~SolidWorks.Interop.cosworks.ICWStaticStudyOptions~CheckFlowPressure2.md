---
title: "CheckFlowPressure2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "CheckFlowPressure2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckFlowPressure2.html"
---

# CheckFlowPressure2 Property (ICWStaticStudyOptions)

Gets or sets whether to import fluid pressure loads from a SOLIDWORKS Flow Simulation results file.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckFlowPressure2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.CheckFlowPressure2 = value

value = instance.CheckFlowPressure2
```

### C#

```csharp
System.bool CheckFlowPressure2 {get; set;}
```

### C++/CLI

```cpp
property System.bool CheckFlowPressure2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to import fluid pressure loads, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::CheckFlowPressure2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~CheckFlowPressure2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
