---
title: "ThreadClass Property (IStraightTapElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightTapElementData"
member: "ThreadClass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~ThreadClass.html"
---

# ThreadClass Property (IStraightTapElementData)

Gets or sets the thread class for this straight tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadClass As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightTapElementData
Dim value As System.Integer

instance.ThreadClass = value

value = instance.ThreadClass
```

### C#

```csharp
System.int ThreadClass {get; set;}
```

### C++/CLI

```cpp
property System.int ThreadClass {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread class as defined in [swStraightTapHoleThreadClass_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightTapHoleThreadClass_e.html)

## VBA Syntax

See [StraightTapElementData::ThreadClass](ms-its:sldworksapivb6.chm::/sldworks~StraightTapElementData~ThreadClass.html).

## Examples

See the [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html) examples.

## Remarks

This property is valid only if [IStraightTapElementData::ThreadClassOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~ThreadClassOverride.html) is set to true.

## See Also

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
