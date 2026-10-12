---
title: "IncludeGlobalFriction2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "IncludeGlobalFriction2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeGlobalFriction2.html"
---

# IncludeGlobalFriction2 Property (ICWStaticStudyOptions)

Gets or sets whether to include global friction.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeGlobalFriction2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.IncludeGlobalFriction2 = value

value = instance.IncludeGlobalFriction2
```

### C#

```csharp
System.bool IncludeGlobalFriction2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeGlobalFriction2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to include global friction, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::IncludeGlobalFriction2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~IncludeGlobalFriction2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
