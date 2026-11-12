---
title: "SetManagedDocument Method (IPDMDocManager)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IPDMDocManager"
member: "SetManagedDocument"
kind: "method"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager~SetManagedDocument.html"
---

# SetManagedDocument Method (IPDMDocManager)

Places the specified document under PDM management.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetManagedDocument( _
   ByVal fileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMDocManager
Dim fileName As System.String
Dim value As System.Boolean

value = instance.SetManagedDocument(fileName)
```

### C#

```csharp
System.bool SetManagedDocument(
   System.string fileName
)
```

### C++/CLI

```cpp
System.bool SetManagedDocument(
   System.String^ fileName
)
```

### Parameters

- `fileName`: Document path and file name; the location in the vault does not need to be writable

### Return Value

True if the managed document is set, false if not

## VBA Syntax

See [PDMDocManager::SetManagedDocument](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~SetManagedDocument.html).

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

## See Also

[IPDMDocManager Interface](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager.html)
[IPDMDocManager Members](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
