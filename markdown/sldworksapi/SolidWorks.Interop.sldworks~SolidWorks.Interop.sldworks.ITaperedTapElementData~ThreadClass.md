---
title: "ThreadClass Property (ITaperedTapElementData)"
project: "SOLIDWORKS API Help"
interface: "ITaperedTapElementData"
member: "ThreadClass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~ThreadClass.html"
---

# ThreadClass Property (ITaperedTapElementData)

Gets or sets the thread class for this tapered tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadClass As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITaperedTapElementData
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

Thread class as defined in [swTaperedTapThreadClass_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTaperedTapThreadClass_e.html)

## VBA Syntax

See [TaperedTapElementData::ThreadClass](ms-its:sldworksapivb6.chm::/sldworks~TaperedTapElementData~ThreadClass.html).

## Examples

See the [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html) examples.

## Remarks

This property is valid only if [ITaperedTapElementData::ThreadClassOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~ThreadClassOverride.html) is set to true.

## See Also

[ITaperedTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html)
[ITaperedTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
