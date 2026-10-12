---
title: "ThreadClassOverride Property (IStraightTapElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightTapElementData"
member: "ThreadClassOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~ThreadClassOverride.html"
---

# ThreadClassOverride Property (IStraightTapElementData)

Gets or sets whether to override the thread class of this straight tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadClassOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightTapElementData
Dim value As System.Boolean

instance.ThreadClassOverride = value

value = instance.ThreadClassOverride
```

### C#

```csharp
System.bool ThreadClassOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool ThreadClassOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the thread class, false to not

## VBA Syntax

See [StraightTapElementData::ThreadClassOverride](ms-its:sldworksapivb6.chm::/sldworks~StraightTapElementData~ThreadClassOverride.html).

## Examples

See the [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html) examples.

## See Also

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html)
[IStraightTapElementData::ThreadClass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~ThreadClass.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
