---
title: "ThreadClassOverride Property (ITaperedTapElementData)"
project: "SOLIDWORKS API Help"
interface: "ITaperedTapElementData"
member: "ThreadClassOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~ThreadClassOverride.html"
---

# ThreadClassOverride Property (ITaperedTapElementData)

Gets or sets whether to override the thread class of this tapered tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadClassOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaperedTapElementData
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

See [TaperedTapElementData::ThreadClassOverride](ms-its:sldworksapivb6.chm::/sldworks~TaperedTapElementData~ThreadClassOverride.html).

## Examples

See the [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html) examples.

## See Also

[ITaperedTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html)
[ITaperedTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData_members.html)
[ITaperedTapElementData::ThreadClass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~ThreadClass.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
