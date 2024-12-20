Title: Object-Oriented Programming
Date: 2024-12-02 12:00
Category: Programming
Tags: pelican, python, design
Summary: Short version for index and feeds.

Let's discuss the basics of OOP. Unlike other programming languages, consectetur adipiscing elit.

<pre class="p-3 text-secondary-emphasis bg-secondary-subtle border border-secondary-subtle rounded-2">
<code>&lt;p&gt;Sample text here...&lt;/p&gt;
&lt;p&gt;And another line of sample text here...&lt;/p&gt;
</code></pre>

<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>

<h2>From Bear</h2><ul>
<li>Describe a single small scenario from a user’s perspective.</li>
<li>Focus on the user’s goal. Not the app itself.</li>
<li>Short, simple, casual. Easily fits on an index card.</li>
</ul><h3>User Story Format</h3><ul>
<li>As a (type of user)</li>
<li>I want (goal)</li>
<li>so that (reason)</li>
</ul><h3>Project Scope</h3><ul>
<li>Keep the scope reasonable for the initial release.</li>
<li>Keep a separate backlog for more features to add later.</li>
</ul><h3>Admin Stories</h3><ul>
<li>Other than end users, what other types of users will there be?</li>
<li>What do application admins want to accomplish?</li>
</ul><h3>User Stories Summary</h3><ul>
<li>Don’t focus on the UI and how tasks are accomplished.</li>
<li>Focus on what and why the user wants to do something.</li>
</ul>
<h2>Use Cases</h2><ul>
<li><b>Title:</b> <i>What</i> is the desired goal?</li>
<li><b>Actor:</b> <i>Who</i> desires it?</li>
<li><b>Scenario:</b> <i>How</i> is it accomplished?</li>
</ul><p>Example</p><ul>
<li><b>Title:</b> Read Tweets about a Twitter Trend</li>
<li><b>Actor:</b> Digest recipient</li>
<li><b>Scenario:</b>
<ul>
<li>Recipient opens the digest email in their email client.</li>
<li>Recipient sees an interesting Twitter trend.</li>
<li>Recipient clicks on the trend link.</li>
<li>The trend link opens a web browser to a page of related tweets.</li>
</ul>
</li>
</ul>
<h2>User Stories vs Use Cases</h2><table>
	<tr>
		<th>User Story</th>
		<th>Use Case</th>
	</tr>
	<tr>
		<td>Who?</td>
		<td>Who?</td>
	</tr>
	<tr>
		<td>What?</td>
		<td>What?</td>
	</tr>
	<tr>
		<td><b>Why?</b></td>
		<td><b>How?</b></td>
	</tr>
</table>
<ul>
<li>For simple projects, user stories might be sufficient.</li>
<li>But for more complex projects, writing out the steps of <i>how</i> a goal will be accomplished by the user can be helpful.</li>
<li>A combination of both is also a perfectly valid way of working.</li>
</ul>
<h2>Requirements</h2><h3>Functional Requirments</h3><ul>
<li><i>What</i> the application must do.</li>
<li>Typically written with sentences that begin with, “The application <i>must</i> or <i>shall</i>…”</li>
</ul><h3>Non-Functional Requirments</h3><ul>
<li><i>How</i> the application should implement the functional requirements.</li>
<li>Typically written as “The applications should be…”</li>
<li>Think in terms of:
<ul>
<li>maintainability</li>
<li>reliability</li>
<li>availability</li>
</ul>
</li>
</ul><p>Examples:</p><ul>
<li>The application should be configurable using an admin GUI.</li>
<li>The application should be extensible to add more content types.</li>
<li>The application should be resilient to content errors.</li>
</ul>
<h2>Program Architecture</h2><h3>Nouns to Classes</h3><p>In terms of object-oriented programming, review the user stories and use cases and <b>look for the nouns</b>:</p><ul>
<li>Quote</li>
<li>Forecast</li>
<li>Location</li>
<li>Trends</li>
<li>Article</li>
<li>Content</li>
<li>Email</li>
<li>Recipients</li>
<li>Time</li>
<li>Credentials</li>
<li>GUI</li>
</ul><p>Evaluate the nouns and look for major groupings. These top-level nouns then become candidates to turn into classes:</p><ul>
<li>Content
<ul>
<li>Quote</li>
<li>Forecast</li>
<li>Location</li>
<li>Trends</li>
<li>Article</li>
</ul>
</li>
<li>Email
<ul>
<li>Recipients</li>
<li>Time</li>
<li>Credentials</li>
</ul>
</li>
<li>GUI</li>
</ul><h3>Verb Phrases to Method Names</h3><ul>
<li>Generate quote</li>
<li>Retrieve forecast</li>
<li>Retrieve trends</li>
<li>Retrieve article</li>
<li>Format content</li>
<li>Send email</li>
<li>Configure content</li>
<li>Add recipients</li>
<li>Remove recipients</li>
<li>Schedule time</li>
<li>Configure credentials</li>
</ul>
<p>Assign each behavior to one of the classes:</p><ul>
<li>Content
<ul>
<li>Generate quote: <code>get_quote()</code></li>
<li>Retrieve forecast: <code>get_forecast()</code></li>
<li>Retrieve trends: <code>get_trends()</code></li>
<li>Retrieve article: <code>get_article()</code></li>
</ul>
</li>
<li>Email
<ul>
<li>Format content: <code>format_message()</code></li>
<li>Send email: <code>send_email()</code></li>
<li>+recipients: List</li>
<li>+send_time: Time</li>
</ul>
</li>
<li>GUI
<ul>
<li>Configure content: <code>config_content()</code></li>
<li>Add recipients: <code>add_recipients()</code></li>
<li>Remove recipients: <code>remove_recipients()</code></li>
<li>Schedule time: <code>schedule_time()</code></li>
<li>Configure credentials: <code>config_credentials()</code></li>
</ul>
</li>
<li>To learn more, check out the <a href='https://www.linkedin.com/learning/programming-foundations-object-oriented-design-3/learn-object-oriented-design-principles?u=114791156'>Programming Foundations: Object-Oriented Design</a> course on LinkedIn Learning.</li>
</ul>
<h2>Stub Code</h2><p>Write out methods with <code>pass</code> as a placeholder. For example, the <code>dd_content.py</code> file starts as:</p>
<pre class="p-3 text-secondary-emphasis bg-secondary-subtle border border-secondary-subtle rounded-2"><code>def get_random_quote():
    pass

def get_weather_forecast():
    pass

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass

if __name__ == '__main__':
    pass # test code</code></pre>
<p><code>dd_email.py</code> starts like this:</p>

<pre class="p-3 text-secondary-emphasis bg-secondary-subtle border border-secondary-subtle rounded-2">
<code>class DailyDigestEmail:

    def __init__(self):
        pass

    def send_email(self):
        pass

    def format_message(self):
        pass

if __name__ == '__main__':
    pass # test code
</code></pre>
<p><code>dd_gui.py</code> starts like this:</p>

<pre class="p-3 text-secondary-emphasis bg-secondary-subtle border border-secondary-subtle rounded-2">
<code>from tkinter import *
from tkinter import ttk

class DailyDigestGUI:

    def __init__(self, root):
        pass # build the GUI

    """
    The GUI should enable the admin to...
        - configure which content sources to include in email
        - add recipients
        - remove recipients
        - schedule daily time to send email
        - configure sender credentials
    """

if __name__ == '__main__':
    root = Tk()
    app = DailyDigestGUI(root)
    root.mainloop()
</code></pre>
