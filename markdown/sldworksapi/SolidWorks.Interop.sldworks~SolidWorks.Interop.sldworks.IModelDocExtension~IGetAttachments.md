---
title: "IGetAttachments Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetAttachments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.html"
---

# IGetAttachments Method (IModelDocExtension)

Gets the attachments for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAttachments( _
   ByVal NumAttachments As System.Integer, _
   ByRef LinkedArr As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim NumAttachments As System.Integer
Dim LinkedArr As System.Boolean
Dim value As System.String

value = instance.IGetAttachments(NumAttachments, LinkedArr)
```

### C#

```csharp
System.string IGetAttachments(
   System.int NumAttachments,
   out System.bool LinkedArr
)
```

### C++/CLI

```cpp
System.String^ IGetAttachments(
   System.int NumAttachments,
   [Out] System.bool LinkedArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumAttachments`: Number of attachments for this document
- `LinkedArr`: - in-process, unmanaged C++: Pointer to an array of VARIANT_BOOL values indicating if a document is linked or not

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the attachments for this document

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method is supported by SOLIDWORKS 2005 and later.

Call [IModelDocExtension::GetAttachmentCoun](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAttachmentCount.html)t before calling this method to determine the size of the array.

There is a one-to-one correspondence between the output arrays.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.html)
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.html)
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
