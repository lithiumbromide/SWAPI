---
title: "InitialConditionType Property (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "InitialConditionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~InitialConditionType.html"
---

# InitialConditionType Property (ICWDynamicInitialCondition)

Gets or sets the type of this initial condition.

## Syntax

### Visual Basic (Declaration)

```vb
Property InitialConditionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim value As System.Integer

instance.InitialConditionType = value

value = instance.InitialConditionType
```

### C#

```csharp
System.int InitialConditionType {get; set;}
```

### C++/CLI

```cpp
property System.int InitialConditionType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of initial condition as defined by [swsDynamicInitialConditionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDynamicInitialConditionType_e.html)

## VBA Syntax

See [CWDynamicInitialCondition::InitialConditionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~InitialConditionType.html).

## Examples

See the [ICWDynamicInitialCondition](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html) examples.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
