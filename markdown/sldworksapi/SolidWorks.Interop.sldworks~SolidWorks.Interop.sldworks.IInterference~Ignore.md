---
title: "Ignore Property (IInterference)"
project: "SOLIDWORKS API Help"
interface: "IInterference"
member: "Ignore"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Ignore.html"
---

# Ignore Property (IInterference)

Gets or sets whether to ignore this interference.

## Syntax

### Visual Basic (Declaration)

```vb
Property Ignore As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterference
Dim value As System.Boolean

instance.Ignore = value

value = instance.Ignore
```

### C#

```csharp
System.bool Ignore {get; set;}
```

### C++/CLI

```cpp
property System.bool Ignore {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to ignore this interference, false to not

## VBA Syntax

See [Interference::Ignore](ms-its:sldworksapivb6.chm::/sldworks~Interference~Ignore.html).

## See Also

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.html)
[IInterferenceDetectionMgr::ShowIgnoredInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
