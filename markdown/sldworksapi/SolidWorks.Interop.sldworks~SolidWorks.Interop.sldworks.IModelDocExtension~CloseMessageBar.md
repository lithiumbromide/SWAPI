---
title: "CloseMessageBar Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CloseMessageBar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CloseMessageBar.html"
---

# CloseMessageBar Method (IModelDocExtension)

Closes the specified message bar in this document's window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CloseMessageBar( _
   ByVal Handler As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Handler As System.Object

instance.CloseMessageBar(Handler)
```

### C#

```csharp
void CloseMessageBar(
   System.object Handler
)
```

### C++/CLI

```cpp
void CloseMessageBar(
   System.Object^ Handler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Handler`: [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html)

## VBA Syntax

See [ModelDocExtension::CloseMessageBar](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CloseMessageBar.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
