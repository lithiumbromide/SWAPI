---
title: "GetAttachments Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetAttachments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.html"
---

# GetAttachments Method (IModelDocExtension)

Gets the attachments for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachments( _
   ByRef LinkedVar As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim LinkedVar As System.Object
Dim value As System.Object

value = instance.GetAttachments(LinkedVar)
```

### C#

```csharp
System.object GetAttachments(
   out System.object LinkedVar
)
```

### C++/CLI

```cpp
System.Object^ GetAttachments(
   [Out] System.Object^ LinkedVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LinkedVar`: Array of VARIANT_BOOL values indicating if a document is linked or not

### Return Value

Array of strings of the names of the attachments for this document

## VBA Syntax

See [ModelDocExtension::GetAttachments](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetAttachments.html).

## Remarks

This method is supported by SOLIDWORKS 2005 and later.

There is a one-to-one correspondence between the output arrays.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.html)
[IModelDocExtension::GetAttachmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.html)
[IModelDocExtension::IGetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.html)
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
