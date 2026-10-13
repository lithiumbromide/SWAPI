---
title: "IsFastener Property (IInterference)"
project: "SOLIDWORKS API Help"
interface: "IInterference"
member: "IsFastener"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IsFastener.html"
---

# IsFastener Property (IInterference)

Gets whether this interference includes a fastener or not.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsFastener As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterference
Dim value As System.Boolean

value = instance.IsFastener
```

### C#

```csharp
System.bool IsFastener {get;}
```

### C++/CLI

```cpp
property System.bool IsFastener {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the interference includes a fastener, false if not

## VBA Syntax

See [Interference::IsFastener](ms-its:sldworksapivb6.chm::/sldworks~Interference~IsFastener.html).

## See Also

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.html)
[IInterferenceDetectionMgr::CreateFastenersFolder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
