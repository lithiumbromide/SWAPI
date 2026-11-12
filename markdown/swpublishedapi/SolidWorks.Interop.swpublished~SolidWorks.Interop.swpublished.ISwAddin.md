---
title: "ISwAddin Interface"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwAddin"
member: ""
kind: "interface"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin.html"
---

# ISwAddin Interface

Allows applications to create SOLIDWORKS add-ins.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwAddin
```

### Visual Basic (Usage)

```vb
Dim instance As ISwAddin
```

### C#

```csharp
public interface ISwAddin
```

### C++/CLI

```cpp
public interface class ISwAddin
```

## VBA Syntax

See [SwAddin](ms-its:swpublishedapivb6.chm::/swpublished~SwAddin.html).

## Remarks

To use this interface in a SOLIDWORKS VB.NET or C# macro or add-in, see [ComVisibleAttribute in VB.NET and C# Macros and Add-ins](sldworksapiprogguide.chm::/OVERVIEW/ComVisibleAttribute_in_VSTA_macros.htm).

If you are creating a COM-style addin and are using an MFC CCmdTarget-derived object to implement ISwAddin, you must fully implement ITypeInfo as follows:

- In the declaration of your CCmdTarget-derived class, add:

1.

  ```vb
  DECLARE_OLETYPELIB(<your CCmdTarget-derived class name>)
  ```
2.

  ```vb
  __declspec( dllexport ) virtual BOOL GetDispatchIID(IID* pIID);
  ```

- In your implementation, add:

1.

  ```vb
  IMPLEMENT_OLETYPELIB(<your class name>, LIBID_SldWorks_SWPublished, SOLIDWORKS_type_library_version, 0)  //e.g., 14 for 2007
  ```
2.

  ```vb
  BOOL auAm_c::GetDispatchIID(IID* pIID)
  {
  ```

```vb
            *pIID == IID_ISwAddin;
            return True;
}
```

-

  ```vb
  In your class constructor, add:
  ```

```vb
 EnableTypeLib();
```

See also [Using SwAddin to Create a SOLIDWORKS Add-in](sldworksAPIProgGuide.chm::/OVERVIEW/Using_SwAddin_to_Create_a_SOLIDWORKS_Addin.htm).

This interface is implemented by add-ins of SOLIDWORKS Partners who participate in the [SOLIDWORKS Partner Program](ms-its:sldworksapiprogguide.chm::/GettingStarted/SolidWorks_Partner_Program_2.htm).

## See Also

[ISwAddin Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin_members.html)
[SolidWorks.Interop.swpublished Namespace](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished_namespace.html)
