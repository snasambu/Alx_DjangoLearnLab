```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

> ✅ Note: Keep the triple backticks and “python” for syntax highlighting.  

---

### 3️⃣ Save the file
- Press `Ctrl + S` (or File → Save).  

---

### 4️⃣ Stage, commit, and push
Back in your terminal:

```powershell
git add create.md
git commit -m "Fix create.md to include Book.objects.create example"
git push origin main
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

> ✅ Note: Keep the triple backticks and “python” for syntax highlighting.  

---

### 3️⃣ Save the file
- Press `Ctrl + S` (or File → Save).  

---

### 4️⃣ Stage, commit, and push
Back in your terminal:

```powershell
git add create.md
git commit -m "Fix create.md to include Book.objects.create example"
git push origin main
